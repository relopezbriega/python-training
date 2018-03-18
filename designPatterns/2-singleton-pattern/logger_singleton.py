class Logger(object):
    """A file-based message singleton logger with the following properties

    Attributes:
        file_name: a string representing the full path of the log file to which
    this logger will write its message
    """
    class __Logger(object):
        def __init__(self, file_name):
            self.file_name = file_name

        def __str__(self):
            return "{0!r} {1}".format(self, self.file_name)

        def _write_log(self, level, msg):
            with open(self.file_name, "a") as log_file:
                log_file.write("[{0}] {1}\n".format(level, msg))

        def critical(self, msg):
            self._write_log("CRITICAL", msg)

        def error(self, msg):
            self._write_log("ERROR", msg)

        def warn(self, msg):
            self._write_log("WARN", msg)

        def info(self, msg):
            self._write_log("INFO", msg)

        def debug(self, msg):
            self._write_log("DEBUG", msg)

    instance = None

    def __new__(cls, file_name):
        if not Logger.instance:
            Logger.instance = Logger.__Logger(file_name)
        else:
            Logger.instance.file_name = file_name

        return Logger.instance

    def __getattr__(self, name):
        getattr(self.instance, name)

    def __setattr__(self, name):
        setattr(self.instance, name)

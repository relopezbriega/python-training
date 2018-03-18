from logger_singleton import Logger

logger1 = Logger("/var/log/logger_singleton1.log")
logger1.info("This is an info message")

print("logger1: ", logger1)

print("-----")
logger2 = Logger("/var/log/logger_singleton2.log")
logger2.info("This is an info message")

print("logger1: ", logger1)
print("logger2: ", logger2)

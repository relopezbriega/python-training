def generate_webform(text_field_list=[], checkbox_field_list=[]):
    generated_fields = "\n".join(
        map(lambda x: '{0}:<br><input type="text" name="{0}"><br>'.format(x),
            text_field_list))

    generated_fields += "\n".join(
        map(lambda x: '{0}:<br><input type="checkbox" name="{0}"><br>'
            .format(x), checkbox_field_list))

    return "<form>{fields}</form>".format(fields=generated_fields)


def build_html_form(text_field_list=[], checkbox_field_list=[]):
    with open("form_file.html", 'w') as file:
        file.write("<html><body>{}</body></html>".format(
            generate_webform(text_field_list, checkbox_field_list)))


if __name__ == "__main__":
    text_field_list = ["name", "age", "email", "telephone"]
    checkbox_field_list = ["awesome", "bad"]
    build_html_form(text_field_list, checkbox_field_list)

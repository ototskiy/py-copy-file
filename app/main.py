def copy_file(command: str) -> None:
    if len(command.split()) != 3 or command.split()[0] != "cp":
        return
    file_origin = command.split()[1]
    file_copy = command.split()[2]
    if file_origin == file_copy:
        return
    try:
        with (open(file_origin, "r") as file_in,
              open(file_copy, "w") as file_out):
            file_out.write(file_in.read())
    except FileNotFoundError:
        return

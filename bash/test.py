import bashClass

bh = bashClass.BashClass()

## Success
print("test run single command")
print(bh.run_bash_command('ls'))

print(" ")

## Success
print("test run multiple commands")
print(bh.run_commands_from_list(['ls','man scp']))


print(" ")

## Success
print("test script directory path")
print(bh.script_directory_path())

print(" ")

## Success
print("test script directory files")
print(bh.all_directory_files(bh.script_directory_path()))

print(" ")

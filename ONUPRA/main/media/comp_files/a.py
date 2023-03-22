import subprocess
import sys
import os


def create_output_file(command):
    global compile_error, delete_files
    try:
        subprocess.run(command, shell=True, check=True,
                       stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        compile_error = 0
    except subprocess.CalledProcessError as e:
        compile_error = 1


def run_command(file_name, tests_input, tests_output):
    global compile_error, delete_files
    path = ''
    command = ""
    if file_name.endswith(".py"):
        command = "python " + path + file_name
    elif file_name.endswith(".cpp"):
        command = "g++ " + path + file_name + \
            " -o " + f"{path + file_name[:-4]}.out"
        create_output_file(command)
        command = f"{path + file_name[:-4]}.out"
        delete_files.append(f"{path + file_name[:-4]}.out")
    elif file_name.endswith(".pas"):
        command = "fpc " + path + file_name
        create_output_file(command)
        command = path + file_name[:-4] + ".exe"
        delete_files.append(path + file_name[:-4] + ".exe")
    elif file_name.endswith(".c"):
        command = "gcc " + path + file_name + \
            " -o " + f"{path + file_name[:-2]}.out"
        create_output_file(command)
        command = f"{path + file_name[:-2]}.out"
        delete_files.append(f"{path + file_name[:-4]}.out")
    elif file_name.endswith(".cs"):
        command = "csc " + path + file_name
        create_output_file(command)
        command = "mono " + path + file_name[:-3] + ".exe"
        delete_files.append(path + file_name[:-3] + ".exe")
    elif file_name.endswith(".go"):
        command = "go run " + path + file_name
    elif file_name.endswith(".kt"):
        command = "kotlinc " + path + file_name + \
            f" -include-runtime -d {path + file_name[:-3]}.jar"
        create_output_file(command)
        command = f"java -jar {path + file_name[:-3]}.jar"
        delete_files.append(f"{path + file_name[:-3]}.jar")
    elif file_name.endswith(".php"):
        command = "php " + path + file_name
    elif file_name.endswith(".rb"):
        command = "ruby " + path + file_name
    elif file_name.endswith(".rs"):
        command = "rustc " + path + file_name + \
            f" -o {path + file_name[:-3]}.out"
        create_output_file(command)
        command = f"{path + file_name[:-3]}.out"
        delete_files.append(f"{path + file_name[:-4]}.out")
    elif file_name.endswith(".js"):
        command = "d8 " + path + file_name
    else:
        compile_error = 1
        return "Нет такого языка програмирования"
    # delete_files.append(path + file_name)
    if compile_error == 0:
        for i in range(len(tests_input)):
            try:
                result = subprocess.run(command, input=(tests_input[i] + "\n"), text=True, shell=True,
                                        timeout=10, stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
                if result.stdout.strip() != tests_output[i].strip():
                    print(result.stdout.strip(), tests_output[i].strip())
                    for j in delete_files:
                        os.remove(j)
                    return [((i - 1) / len(tests_input)), f"Неправильный ответ на тесте {i}"]
            except subprocess.TimeoutExpired:
                compile_error = 1
                for j in delete_files:
                    os.remove(j)
                return [((i - 1) / len(tests_input)), f"Превышено ограничение времени на тесте {i}"]
            except subprocess.CalledProcessError:
                compile_error = 1
                for j in delete_files:
                    os.remove(j)
                return [((i - 1) / len(tests_input)), f"Проблема с принятием входных данных на тесте {i}"]
        else:
            return [1, "Все тесты прошли успешно"]
    else:
        for i in delete_files:
            os.remove(i)
        return "Не удалось скомпилировать файл"


delete_files = []
compile_error = 0
file_name = input("Введите имя файла: ")
tests_input = ['1\n2', '2', '3', '4']
print(tests_input[0])
tests_output = ['1\n2', '2', '4', '4']
print(run_command(file_name, tests_input, tests_output))

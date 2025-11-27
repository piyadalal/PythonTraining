"""
demo HOWTO trap error or exception using try except block

"""

import sys



def main():
    import re
    try:
        fh_in = open(r"/Users/prda5207/PycharmProjects/PythonTraining/words.txt", mode="rt")  # 45k lines

        for line in fh_in:
            m = re.search(r"^.{19}", line)  # same pattern repeated for 45k times use precompiled complies pattern only once
            try:
                if m:
                    print(f"Matched {m.group()} on {line.rstrip()} at {m.start()} - {m.end()}")
                    # print(line, end="")
            except AttributeError:
                print("can't find any matched groups")
    except FileNotFoundError as err:
#* `stdout` is **buffered** (stored temporarily before printing)
#`stderr` is **NOT buffered** — prints immediately
        print(err.args, flush=True) # immeidately flushes
        print(f"Error - {err.args[0]}, {err.args[1]}, {err.filename}",file=sys.stderr)
        sys.exit(1)
    except PermissionError as err:
        print(f"Error - {err.args[0]}, {err.args[1]}, {err.filename}", file=sys.stderr)
        sys.exit(2)
    except Exception as err:
        print(f"Some other error occurred - investigate", file=sys.stderr)
        sys.exit(3)
        # err object can display info about error as tuple error code, error msg, filename
        print(err.args) # prints rerdirects to stdout we give to filename : stderr
        #print(f"Error {err.args}")


    return None


if __name__ == "__main__":
    main()
    sys.exit(0)

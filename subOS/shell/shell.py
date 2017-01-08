import cmd


class Shell(cmd.Cmd):

    """
    This is the Shell for subOS, it can be interactive or Command
    This Shell is made from cmd module
    """

    def do_echo(self, *args):
        string = ''.join(args)
        print(string)

    def do_input(self, inp):
        tok = inp.split(',')
        prompt = tok[0]
        var = tok[1]
        # prompt = args[0]
        # var = args[1]
        exec(var + ' = raw_input("' + prompt + '")')

Shell = Shell()
Shell.cmdloop()

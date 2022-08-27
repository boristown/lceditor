import sys
import os
def run(in_path):
    back_frame = sys._getframe().f_back
    back_filename = os.path.basename(back_frame.f_code.co_filename)
    back_module_name = back_filename[:-3]
    back_module=__import__(back_module_name)
    dirs = dir(back_module)
    if "Solution" in dirs:
        cls = getattr(back_module,"Solution")
        funcname = dir(cls)[-1]
        solu = cls()
        func = getattr(solu,funcname)
        param_cnt = func.__code__.co_argcount-1
        with open(in_path,"r") as infile:
            lines = infile.readlines()
        sample_cnt = len(lines) // param_cnt
        ind = 0
        for _ in range(sample_cnt):
            params = []
            for _ in range(param_cnt):
                params.append(eval(lines[ind]))
                ind += 1
            ans = func(*params)
            print(ans)
    else:
        with open(in_path,"r") as infile:
            lines = infile.readlines()
        if len(lines) == 2:
            funcnames = eval(lines[0])
            funcparams = eval(lines[1])
            classname = funcnames[0]
            classparam = funcparams[0]
            funcnames = funcnames[1:]
            funcparams = funcparams[1:]
            strparam = ",".join(map(str,classparam))
            code = "import "+back_module_name+"\n"
            code += "sol = "+back_module_name+"." + str(classname) + "("+strparam+")\n"
            code += "ans = [None]\n"
            for fun,par in zip(funcnames,funcparams):
                strparam = ",".join(map(str,par))
                code+="ans.append(sol."+str(fun)+"("+strparam+"))\n"
            code += "print(ans)"
            exec(code)
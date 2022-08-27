import sys
import os
def run():
    back_frame = sys._getframe().f_back
    back_filename = os.path.basename(back_frame.f_code.co_filename)
    back_funcname = back_frame.f_code.co_name
    back_lineno = back_frame.f_lineno

    print(back_filename)
    print(back_funcname)
    print(back_lineno)
    module_t=__import__(back_filename[:-3])
    #import leetcode
    dirs = dir(module_t)
    if "Solution" in dirs:
        cls = getattr(module_t,"Solution")
        funcname = dir(cls)[-1]
        solu = cls()
        func = getattr(solu,funcname)
        param_cnt = func.__code__.co_argcount-1
        with open("in.txt","r") as infile:
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
        with open("in.txt","r") as infile:
            lines = infile.readlines()
        if len(lines) == 2:
            funcnames = eval(lines[0])
            funcparams = eval(lines[1])
            classname = funcnames[0]
            classparam = funcparams[0]
            funcnames = funcnames[1:]
            funcparams = funcparams[1:]
            strparam = ",".join(map(str,classparam))
            code = "sol = "+back_filename[:-3]+"." + str(classname) + "("+strparam+")\n"
            code += "ans = [None]\n"
            for fun,par in zip(funcnames,funcparams):
                strparam = ",".join(map(str,par))
                code+="ans.append(sol."+str(fun)+"("+strparam+"))\n"
            code += "print(ans)"
            exec(code)
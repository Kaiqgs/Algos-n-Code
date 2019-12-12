
def import_files_now(fname, output="", usedfiles=[]):    
    with open(fname, "r") as f:
        if(output == ""):
            output = f.read()
        else:
            output =  f.read() + "\n" + output
        usedfiles.append(fname)
    
    # print("~~~~~~~~~~~~~~")
    # print(output)
    # print("~~~~~~~~~~~~~~")
    
    importidx = 1
    while importidx > 0:
        importidx = output.find("import")
        if(importidx == -1):
            break
        
        openquotes = output.find("\"", importidx)
        endquotes = output.find("\"", openquotes+1)
        nfname = output[openquotes+1:endquotes]
        
        #print("fname:",nfname)
        output = output[:importidx] + output[endquotes+1:]
        if(nfname in usedfiles):
            continue
        else:
            return import_files_now(nfname, output=output, usedfiles=usedfiles)
    
    return output

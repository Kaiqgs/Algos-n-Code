from App.Grammar.PapeteParser import PapeteParser
import antlr4
import sys
import warnings


class NotDefinedError(Exception):
    def __init__(self, varname, errors=""):
        super().__init__(f"Variable {varname} isn't defined!")


class MemoryHandler:
    def __init__(self):
        self.FUNC_TYPE = "func"
        self.GLOBAL_SCOPE = None
        self.variables = {}

    def getValue(self, var):
        scope = self.getScope(var)
        id_ = self._variableIdentifier(var, scope)
        while scope != self.GLOBAL_SCOPE and id_ not in self.variables:
            scope = self.getScope(scope.parentCtx)
            id_ = self._variableIdentifier(var, scope)

        if(id_ in self.variables):
            return self.variables[id_]["value"]
        raise NotDefinedError(id_[0])

    def getScope(self, ctx):
        pointer = ctx
        isstmt = issubclass(pointer.__class__, PapeteParser.StmtContext)
        while(pointer is not None and not isstmt):
            pointer = pointer.parentCtx
            isstmt = issubclass(pointer.__class__, PapeteParser.StmtContext)
        return pointer

    def defineFunc(self, ctx: PapeteParser.DeclFuncContext):
        id_ = self.defineVariable(ctx.VAR(), self.FUNC_TYPE)
        val = ctx.paramblock(), ctx.stmt()
        self.assignVariable(id_, val)

    def defineVariables(self, vars_: list, types: list, customscope=None):
        for var, typ in zip(vars_, types):
            yield self.defineVariable(var, typ, customscope=customscope)

    def defineVariable(self, var, type_, customscope=None):
        if customscope is None:
            scope = self.getScope(var)
        else:
            scope = customscope
        id_ = self._variableIdentifier(var, scope)
        if(id_ in self.variables):
            pass
            #warnings.warn(f"You're re-defining the variable {var.getText()}!")
        self.variables[id_] = self._variableProperties(type_=type_)
        return id_
    
    

    def assignVariables(self, ids_, vals):
        for id_, val in zip(ids_, vals):
            self.assignVariable(id_, val)

    def assignVariable(self, id_, val):
        if(id_ in self.variables):
            type_ = self.variables[id_]["type"]
            if(type_ == "int"):
                if(isinstance(val, str) and len(val) <=1):
                    val = ord(val)
                else:
                    val = int(val)
            elif(type_ == "string"):
                val = str(val)
            elif(type_ == "char"):
                if(isinstance(val, int)):
                    val = chr(val)
                else:
                    val = str(val)[0]
            elif(type_=="bool"):
                val = bool(val)
            elif(type_ == "double"):
                val = float(val)
            self.variables[id_]["value"] = val
        else:
            
            raise NotDefinedError(id_[0])

    def assignScopelessVariable(self, var, val):
        
        id_ = self.findVariable(var)
        self.assignVariable(id_, val)


    
    def findVariable(self, var):
        scope = self.getScope(var)
        id_ = self._variableIdentifier(var, scope)
        while scope != self.GLOBAL_SCOPE and id_ not in self.variables:
            scope = self.getScope(scope.parentCtx)
            id_ = self._variableIdentifier(var, scope)
        if(id_ in self.variables):
            return id_
        else:
            raise NotDefinedError(var.getText())

    def setMultipleScopes(self, vars_, ids_,  newscopes):
        for var, id_, nscope in zip(vars_, ids_, newscopes):
            self.setScope(var, id_, nscope)

    def setScope(self, var, id_, scope):
        if(not self._variableExist(id_)):
            raise NotDefinedError(id_[0])
        else:

            newid_ = self._variableIdentifier(var, scope)
            self.variables[newid_] = self.variables[id_]
            del self.variables[id_]

    def _variableExist(self, id_):
        return id_ in self.variables

    def _variableIdentifier(self, var, scope):
        return (var.getText(), scope)

    def _variableProperties(self, type_=None):
        return {"value": None, "type": type_}

    

    def __repr__(self):
        val = ""
        for k, v in self.variables.items():
            var, scope = k
            varval = v['value']
            if(v['type'] == self.FUNC_TYPE):
                varval = "__func__"
            val += f"{v['type']:>6} {str(var):<15} = {str(varval):^55} at scope {str(scope):^25}\n"

        return val

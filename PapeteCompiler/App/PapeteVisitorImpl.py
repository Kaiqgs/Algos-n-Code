from App.Grammar.PapeteVisitor import PapeteVisitor
from App.Grammar.PapeteParser import PapeteParser
from App.Grammar.PapeteListener import PapeteListener
from App.MemoryHandler import MemoryHandler
import antlr4


def log(*msg, **kwargs):
    # return
    print(*msg, **kwargs)


def anyis(t, x, y):
    return isinstance(x, t) or isinstance(y, t)


class PapeteVisitorImpl(PapeteVisitor):
    def x(self):
        antlr4.ParserRuleContext().getsou

    def __init__(self, vhandler: MemoryHandler = MemoryHandler()):
        super().__init__()
        self.mhandler = vhandler
        self.declaration_function_flag = None
        self.return_related = "___*___here's a return___*___"

    """
        Utils:
    """

    def isReturnRelated(self, val):
        if(val is not None):
            if(self.return_related in val):
                return True
        return False

    """
        Types:
    """

    def visitTypeInt(self, ctx: PapeteParser.TypeIntContext):
        return ctx.INT_TYPE().getText()

    def visitTypeDouble(self, ctx: PapeteParser.TypeDoubleContext):
        return ctx.DOUBLE_TYPE().getText()

    def visitTypeString(self, ctx: PapeteParser.TypeStringContext):
        return ctx.STRING_TYPE().getText()

    def visitTypeBool(self, ctx: PapeteParser.TypeBoolContext):
        return ctx.BOOL_TYPE().getText()

    def visitTypeVoid(self, ctx: PapeteParser.TypeVoidContext):
        return ctx.VOID_TYPE().getText()

    def visitTypeChar(self, ctx: PapeteParser.TypeCharContext):
        return ctx.CHAR_TYPE().getText()

    def visitTypeFunc(self, ctx: PapeteParser.TypeFuncContext):
        return ctx.FUNCTOK().getText()
    """
        Operations:
    """

    def visitOperationPlus(self, ctx: PapeteParser.OperationPlusContext):
        def add(x, y):
            if(anyis(str, x, y)):
                return str(x) + str(y)
            else:
                return x+y
        return add

    def visitOperationMinus(self, ctx: PapeteParser.OperationMinusContext):
        return lambda x, y: x-y

    def visitOperationTimes(self, ctx: PapeteParser.OperationTimesContext):
        return lambda x, y: x*y

    def visitOperationDiv(self, ctx: PapeteParser.OperationDivContext):
        return lambda x, y: x/y

    def visitOperationMod(self, ctx: PapeteParser.OperationModContext):
        return lambda x, y: x % y

    def visitOperationEe(self, ctx: PapeteParser.OperationEeContext):
        return lambda x, y: x == y

    def visitOperationNe(self, ctx: PapeteParser.OperationNeContext):
        return lambda x, y: x != y

    def visitOperationGt(self, ctx: PapeteParser.OperationGtContext):
        return lambda x, y: x > y

    def visitOperationGe(self, ctx: PapeteParser.OperationGeContext):
        return lambda x, y: x >= y

    def visitOperationLt(self, ctx: PapeteParser.OperationLtContext):
        return lambda x, y: x < y

    def visitOperationLe(self, ctx: PapeteParser.OperationLeContext):
        return lambda x, y: x <= y

    def visitOperationAnd(self, ctx: PapeteParser.OperationAndContext):
        return lambda x, y: x and y

    def visitOperationOr(self, ctx: PapeteParser.OperationOrContext):
        return lambda x, y: x or y

    """
        ExpressionBlock:
    """

    def visitExprblock(self, ctx: PapeteParser.ExprblockContext):
        return self.visit(ctx.expr())

    """
        Facts:
    """

    def visitFactVar(self, ctx: PapeteParser.FactVarContext):
        return self.mhandler.getValue(ctx.VAR())

    def visitFactNum(self, ctx: PapeteParser.FactNumContext):
        v = ctx.NUM().getText()
        if(v[0] == "_"):
            v = "-" + v[1:]
        return float(v)

    def visitFactString(self, ctx: PapeteParser.FactStringContext):
        return ctx.STRING().getText()[1:-1]

    def visitFactChar(self, ctx: PapeteParser.FactCharContext):
        return ctx.CHAR().getText()[1:-1]

    def visitFactTrue(self, ctx: PapeteParser.FactTrueContext):
        return ctx.TRUE().getText() == "true"

    def visitFactFalse(self, ctx: PapeteParser.FactFalseContext):
        return ctx.FALSE().getText() == "false"

    """
        ArgsBlock:
    """

    def visitArgsblock(self, ctx: PapeteParser.ArgsblockContext):
        return [self.visit(exp) for exp in ctx.expr()]

    def visitArgs(self, ctx: PapeteParser.ArgsContext):
        return ctx.VAR()

    """
        Assignments:
    """

    def visitAssgDeclVar(self, ctx: PapeteParser.AssgDeclVarContext):
        vars_, types, ids_ = self.visit(ctx.decl())
        vals = [self.visit(ctx.expr())] * len(vars_)
        self.mhandler.assignVariables(ids_, vals)

    def visitAssgVar(self, ctx: PapeteParser.AssgVarContext):
        var = ctx.VAR()
        val = self.visit(ctx.expr())
        self.mhandler.assignScopelessVariable(var, val)

    """
        ParamBlock:
    """

    def visitParamblock(self, ctx: PapeteParser.ParamblockContext):
        return ctx.decl()

    """
        Declarations:
    """

    def visitDeclMultTypeVar(self, ctx: PapeteParser.DeclMultTypeVarContext):
        #log("defining", ctx.getText())
        types = [self.visit(type_) for type_ in ctx.type_()]
        vars_ = list(ctx.VAR())
        ids_ = list(self.mhandler.defineVariables(
            vars_, types, customscope=self.declaration_function_flag))
        self.declaration_function_flag = None
        return vars_, types, ids_

    def visitDeclTypeMultVar(self, ctx: PapeteParser.DeclTypeMultVarContext):
        #log("defining", ctx.getText())
        vars_ = list(self.visit(ctx.args()))
        types = [self.visit(ctx.type_())] * len(vars_)

        ids_ = list(self.mhandler.defineVariables(
            vars_, types, customscope=self.declaration_function_flag))
        self.declaration_function_flag = None
        return vars_, types, ids_

    def visitDeclFunc(self, ctx: PapeteParser.DeclFuncContext):
        self.mhandler.defineFunc(ctx)
        return super().visitDeclFunc(ctx)

    """
        Calls:
    """

    def visitCallFunc(self, ctx: PapeteParser.CallFuncContext):
        paramblock, stmt = self.mhandler.getValue(ctx.VAR())
        self.declaration_function_flag = stmt
        decl = self.visit(paramblock)

        if(len(decl) > 0):
            # Get arguments;
            argsvals = self.visit(ctx.argsblock())

            # Declare arguments;
            declargsids = [self.visit(declaration)
                           for declaration in decl][0][2]

            self.mhandler.assignVariables(ids_=declargsids, vals=argsvals)

        # Run stmt;
        didreturn, retval = self.chooseVisitStmt(stmt)

        return retval

    def visitCallReturnTok(self, ctx: PapeteParser.CallReturnTokContext):
        return self.visit(ctx.expr())

    def visitCallRead(self, ctx: PapeteParser.CallReadContext):
        return input()

    def visitCallPrint(self, ctx: PapeteParser.CallPrintContext):
        x = "".join([str(arg) for arg in self.visit(ctx.argsblock())])
        print(x)
        pass

    """
        Statement;
    """

    def visitStmt(self, ctx: PapeteParser.StmtContext):
        pass

    def chooseVisitStmt(self, ctx: PapeteParser.StmtContext):
        for line in ctx.line():
            iscall = issubclass(
                line.__class__, PapeteParser.LineCallContext)

            if(iscall):
                line = line.getChild(0)
                isreturn = issubclass(
                    line.__class__, PapeteParser.CallReturnTokContext
                )

                if(isreturn):
                    retval = self.visit(line)
                    return self.return_related, retval

            value = self.visit(line)
            if(self.isReturnRelated(value)):
                return self.return_related, value[1]

        return False, None

    """
        Conditionals:
    """

    def visitCond(self, ctx: PapeteParser.CondContext):
        condition = self.visit(ctx.exprblock())
        if(condition):
            return self.chooseVisitStmt(ctx.stmt()[0])
        else:
            if(len(ctx.stmt()) > 1):
                return self.chooseVisitStmt(ctx.stmt()[1])

        #log("Condition", condition)

    """
        Expressions:
    """

    def visitLoop(self, ctx: PapeteParser.LoopContext):
        stmt = ctx.stmt()
        while bool(self.visit(ctx.exprblock())):
            retval = self.chooseVisitStmt(stmt)
            if(self.isReturnRelated(retval)):
                return retval

    def visitLineCall(self, ctx):
        return super().visitLineCall(ctx)
        raise Exception("funcionou")

    def visitExprOperationFact(self, ctx: PapeteParser.ExprOperationFactContext):

        op = self.visit(ctx.operation())
        exprval = self.visit(ctx.expr())
        factval = self.visit(ctx.fact())

        #log(f"Left:{str(exprval):^15} as {str(type(exprval)):^15} {ctx.operation().getText()} Right:{str(factval):^15} as {str(type(factval)):^15}")
        return op(exprval, factval)

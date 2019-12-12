# Generated from App/Grammar/Papete.g4 by ANTLR 4.7.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .PapeteParser import PapeteParser
else:
    from PapeteParser import PapeteParser

# This class defines a complete generic visitor for a parse tree produced by PapeteParser.

class PapeteVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by PapeteParser#import_.
    def visitImport_(self, ctx:PapeteParser.Import_Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PapeteParser#prog.
    def visitProg(self, ctx:PapeteParser.ProgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PapeteParser#LineAssg.
    def visitLineAssg(self, ctx:PapeteParser.LineAssgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PapeteParser#LineDecl.
    def visitLineDecl(self, ctx:PapeteParser.LineDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PapeteParser#LineCall.
    def visitLineCall(self, ctx:PapeteParser.LineCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PapeteParser#LineCond.
    def visitLineCond(self, ctx:PapeteParser.LineCondContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PapeteParser#LineLoop.
    def visitLineLoop(self, ctx:PapeteParser.LineLoopContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PapeteParser#paramblock.
    def visitParamblock(self, ctx:PapeteParser.ParamblockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PapeteParser#argsblock.
    def visitArgsblock(self, ctx:PapeteParser.ArgsblockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PapeteParser#exprblock.
    def visitExprblock(self, ctx:PapeteParser.ExprblockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PapeteParser#loop.
    def visitLoop(self, ctx:PapeteParser.LoopContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PapeteParser#cond.
    def visitCond(self, ctx:PapeteParser.CondContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PapeteParser#CallFunc.
    def visitCallFunc(self, ctx:PapeteParser.CallFuncContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PapeteParser#CallRead.
    def visitCallRead(self, ctx:PapeteParser.CallReadContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PapeteParser#CallPrint.
    def visitCallPrint(self, ctx:PapeteParser.CallPrintContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PapeteParser#CallReturnTok.
    def visitCallReturnTok(self, ctx:PapeteParser.CallReturnTokContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PapeteParser#args.
    def visitArgs(self, ctx:PapeteParser.ArgsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PapeteParser#AssgDeclVar.
    def visitAssgDeclVar(self, ctx:PapeteParser.AssgDeclVarContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PapeteParser#AssgVar.
    def visitAssgVar(self, ctx:PapeteParser.AssgVarContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PapeteParser#DeclMultTypeVar.
    def visitDeclMultTypeVar(self, ctx:PapeteParser.DeclMultTypeVarContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PapeteParser#DeclTypeMultVar.
    def visitDeclTypeMultVar(self, ctx:PapeteParser.DeclTypeMultVarContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PapeteParser#DeclFunc.
    def visitDeclFunc(self, ctx:PapeteParser.DeclFuncContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PapeteParser#ExprOperationFact.
    def visitExprOperationFact(self, ctx:PapeteParser.ExprOperationFactContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PapeteParser#ExprFact.
    def visitExprFact(self, ctx:PapeteParser.ExprFactContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PapeteParser#stmt.
    def visitStmt(self, ctx:PapeteParser.StmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PapeteParser#FactVar.
    def visitFactVar(self, ctx:PapeteParser.FactVarContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PapeteParser#FactNum.
    def visitFactNum(self, ctx:PapeteParser.FactNumContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PapeteParser#FactString.
    def visitFactString(self, ctx:PapeteParser.FactStringContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PapeteParser#FactChar.
    def visitFactChar(self, ctx:PapeteParser.FactCharContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PapeteParser#FactTrue.
    def visitFactTrue(self, ctx:PapeteParser.FactTrueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PapeteParser#FactFalse.
    def visitFactFalse(self, ctx:PapeteParser.FactFalseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PapeteParser#FactCall.
    def visitFactCall(self, ctx:PapeteParser.FactCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PapeteParser#FactExprBlock.
    def visitFactExprBlock(self, ctx:PapeteParser.FactExprBlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PapeteParser#OperationPlus.
    def visitOperationPlus(self, ctx:PapeteParser.OperationPlusContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PapeteParser#OperationMinus.
    def visitOperationMinus(self, ctx:PapeteParser.OperationMinusContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PapeteParser#OperationTimes.
    def visitOperationTimes(self, ctx:PapeteParser.OperationTimesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PapeteParser#OperationDiv.
    def visitOperationDiv(self, ctx:PapeteParser.OperationDivContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PapeteParser#OperationMod.
    def visitOperationMod(self, ctx:PapeteParser.OperationModContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PapeteParser#OperationEe.
    def visitOperationEe(self, ctx:PapeteParser.OperationEeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PapeteParser#OperationNe.
    def visitOperationNe(self, ctx:PapeteParser.OperationNeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PapeteParser#OperationGt.
    def visitOperationGt(self, ctx:PapeteParser.OperationGtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PapeteParser#OperationGe.
    def visitOperationGe(self, ctx:PapeteParser.OperationGeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PapeteParser#OperationLt.
    def visitOperationLt(self, ctx:PapeteParser.OperationLtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PapeteParser#OperationLe.
    def visitOperationLe(self, ctx:PapeteParser.OperationLeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PapeteParser#OperationAnd.
    def visitOperationAnd(self, ctx:PapeteParser.OperationAndContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PapeteParser#OperationOr.
    def visitOperationOr(self, ctx:PapeteParser.OperationOrContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PapeteParser#TypeInt.
    def visitTypeInt(self, ctx:PapeteParser.TypeIntContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PapeteParser#TypeDouble.
    def visitTypeDouble(self, ctx:PapeteParser.TypeDoubleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PapeteParser#TypeString.
    def visitTypeString(self, ctx:PapeteParser.TypeStringContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PapeteParser#TypeBool.
    def visitTypeBool(self, ctx:PapeteParser.TypeBoolContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PapeteParser#TypeVoid.
    def visitTypeVoid(self, ctx:PapeteParser.TypeVoidContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PapeteParser#TypeChar.
    def visitTypeChar(self, ctx:PapeteParser.TypeCharContext):
        return self.visitChildren(ctx)



del PapeteParser
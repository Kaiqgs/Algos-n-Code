# Generated from App/Grammar/Papete.g4 by ANTLR 4.7.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .PapeteParser import PapeteParser
else:
    from PapeteParser import PapeteParser

# This class defines a complete listener for a parse tree produced by PapeteParser.
class PapeteListener(ParseTreeListener):

    # Enter a parse tree produced by PapeteParser#import_.
    def enterImport_(self, ctx:PapeteParser.Import_Context):
        pass

    # Exit a parse tree produced by PapeteParser#import_.
    def exitImport_(self, ctx:PapeteParser.Import_Context):
        pass


    # Enter a parse tree produced by PapeteParser#prog.
    def enterProg(self, ctx:PapeteParser.ProgContext):
        pass

    # Exit a parse tree produced by PapeteParser#prog.
    def exitProg(self, ctx:PapeteParser.ProgContext):
        pass


    # Enter a parse tree produced by PapeteParser#LineAssg.
    def enterLineAssg(self, ctx:PapeteParser.LineAssgContext):
        pass

    # Exit a parse tree produced by PapeteParser#LineAssg.
    def exitLineAssg(self, ctx:PapeteParser.LineAssgContext):
        pass


    # Enter a parse tree produced by PapeteParser#LineDecl.
    def enterLineDecl(self, ctx:PapeteParser.LineDeclContext):
        pass

    # Exit a parse tree produced by PapeteParser#LineDecl.
    def exitLineDecl(self, ctx:PapeteParser.LineDeclContext):
        pass


    # Enter a parse tree produced by PapeteParser#LineCall.
    def enterLineCall(self, ctx:PapeteParser.LineCallContext):
        pass

    # Exit a parse tree produced by PapeteParser#LineCall.
    def exitLineCall(self, ctx:PapeteParser.LineCallContext):
        pass


    # Enter a parse tree produced by PapeteParser#LineCond.
    def enterLineCond(self, ctx:PapeteParser.LineCondContext):
        pass

    # Exit a parse tree produced by PapeteParser#LineCond.
    def exitLineCond(self, ctx:PapeteParser.LineCondContext):
        pass


    # Enter a parse tree produced by PapeteParser#LineLoop.
    def enterLineLoop(self, ctx:PapeteParser.LineLoopContext):
        pass

    # Exit a parse tree produced by PapeteParser#LineLoop.
    def exitLineLoop(self, ctx:PapeteParser.LineLoopContext):
        pass


    # Enter a parse tree produced by PapeteParser#paramblock.
    def enterParamblock(self, ctx:PapeteParser.ParamblockContext):
        pass

    # Exit a parse tree produced by PapeteParser#paramblock.
    def exitParamblock(self, ctx:PapeteParser.ParamblockContext):
        pass


    # Enter a parse tree produced by PapeteParser#argsblock.
    def enterArgsblock(self, ctx:PapeteParser.ArgsblockContext):
        pass

    # Exit a parse tree produced by PapeteParser#argsblock.
    def exitArgsblock(self, ctx:PapeteParser.ArgsblockContext):
        pass


    # Enter a parse tree produced by PapeteParser#exprblock.
    def enterExprblock(self, ctx:PapeteParser.ExprblockContext):
        pass

    # Exit a parse tree produced by PapeteParser#exprblock.
    def exitExprblock(self, ctx:PapeteParser.ExprblockContext):
        pass


    # Enter a parse tree produced by PapeteParser#loop.
    def enterLoop(self, ctx:PapeteParser.LoopContext):
        pass

    # Exit a parse tree produced by PapeteParser#loop.
    def exitLoop(self, ctx:PapeteParser.LoopContext):
        pass


    # Enter a parse tree produced by PapeteParser#cond.
    def enterCond(self, ctx:PapeteParser.CondContext):
        pass

    # Exit a parse tree produced by PapeteParser#cond.
    def exitCond(self, ctx:PapeteParser.CondContext):
        pass


    # Enter a parse tree produced by PapeteParser#CallFunc.
    def enterCallFunc(self, ctx:PapeteParser.CallFuncContext):
        pass

    # Exit a parse tree produced by PapeteParser#CallFunc.
    def exitCallFunc(self, ctx:PapeteParser.CallFuncContext):
        pass


    # Enter a parse tree produced by PapeteParser#CallRead.
    def enterCallRead(self, ctx:PapeteParser.CallReadContext):
        pass

    # Exit a parse tree produced by PapeteParser#CallRead.
    def exitCallRead(self, ctx:PapeteParser.CallReadContext):
        pass


    # Enter a parse tree produced by PapeteParser#CallPrint.
    def enterCallPrint(self, ctx:PapeteParser.CallPrintContext):
        pass

    # Exit a parse tree produced by PapeteParser#CallPrint.
    def exitCallPrint(self, ctx:PapeteParser.CallPrintContext):
        pass


    # Enter a parse tree produced by PapeteParser#CallReturnTok.
    def enterCallReturnTok(self, ctx:PapeteParser.CallReturnTokContext):
        pass

    # Exit a parse tree produced by PapeteParser#CallReturnTok.
    def exitCallReturnTok(self, ctx:PapeteParser.CallReturnTokContext):
        pass


    # Enter a parse tree produced by PapeteParser#args.
    def enterArgs(self, ctx:PapeteParser.ArgsContext):
        pass

    # Exit a parse tree produced by PapeteParser#args.
    def exitArgs(self, ctx:PapeteParser.ArgsContext):
        pass


    # Enter a parse tree produced by PapeteParser#AssgDeclVar.
    def enterAssgDeclVar(self, ctx:PapeteParser.AssgDeclVarContext):
        pass

    # Exit a parse tree produced by PapeteParser#AssgDeclVar.
    def exitAssgDeclVar(self, ctx:PapeteParser.AssgDeclVarContext):
        pass


    # Enter a parse tree produced by PapeteParser#AssgVar.
    def enterAssgVar(self, ctx:PapeteParser.AssgVarContext):
        pass

    # Exit a parse tree produced by PapeteParser#AssgVar.
    def exitAssgVar(self, ctx:PapeteParser.AssgVarContext):
        pass


    # Enter a parse tree produced by PapeteParser#DeclMultTypeVar.
    def enterDeclMultTypeVar(self, ctx:PapeteParser.DeclMultTypeVarContext):
        pass

    # Exit a parse tree produced by PapeteParser#DeclMultTypeVar.
    def exitDeclMultTypeVar(self, ctx:PapeteParser.DeclMultTypeVarContext):
        pass


    # Enter a parse tree produced by PapeteParser#DeclTypeMultVar.
    def enterDeclTypeMultVar(self, ctx:PapeteParser.DeclTypeMultVarContext):
        pass

    # Exit a parse tree produced by PapeteParser#DeclTypeMultVar.
    def exitDeclTypeMultVar(self, ctx:PapeteParser.DeclTypeMultVarContext):
        pass


    # Enter a parse tree produced by PapeteParser#DeclFunc.
    def enterDeclFunc(self, ctx:PapeteParser.DeclFuncContext):
        pass

    # Exit a parse tree produced by PapeteParser#DeclFunc.
    def exitDeclFunc(self, ctx:PapeteParser.DeclFuncContext):
        pass


    # Enter a parse tree produced by PapeteParser#ExprOperationFact.
    def enterExprOperationFact(self, ctx:PapeteParser.ExprOperationFactContext):
        pass

    # Exit a parse tree produced by PapeteParser#ExprOperationFact.
    def exitExprOperationFact(self, ctx:PapeteParser.ExprOperationFactContext):
        pass


    # Enter a parse tree produced by PapeteParser#ExprFact.
    def enterExprFact(self, ctx:PapeteParser.ExprFactContext):
        pass

    # Exit a parse tree produced by PapeteParser#ExprFact.
    def exitExprFact(self, ctx:PapeteParser.ExprFactContext):
        pass


    # Enter a parse tree produced by PapeteParser#stmt.
    def enterStmt(self, ctx:PapeteParser.StmtContext):
        pass

    # Exit a parse tree produced by PapeteParser#stmt.
    def exitStmt(self, ctx:PapeteParser.StmtContext):
        pass


    # Enter a parse tree produced by PapeteParser#FactVar.
    def enterFactVar(self, ctx:PapeteParser.FactVarContext):
        pass

    # Exit a parse tree produced by PapeteParser#FactVar.
    def exitFactVar(self, ctx:PapeteParser.FactVarContext):
        pass


    # Enter a parse tree produced by PapeteParser#FactNum.
    def enterFactNum(self, ctx:PapeteParser.FactNumContext):
        pass

    # Exit a parse tree produced by PapeteParser#FactNum.
    def exitFactNum(self, ctx:PapeteParser.FactNumContext):
        pass


    # Enter a parse tree produced by PapeteParser#FactString.
    def enterFactString(self, ctx:PapeteParser.FactStringContext):
        pass

    # Exit a parse tree produced by PapeteParser#FactString.
    def exitFactString(self, ctx:PapeteParser.FactStringContext):
        pass


    # Enter a parse tree produced by PapeteParser#FactChar.
    def enterFactChar(self, ctx:PapeteParser.FactCharContext):
        pass

    # Exit a parse tree produced by PapeteParser#FactChar.
    def exitFactChar(self, ctx:PapeteParser.FactCharContext):
        pass


    # Enter a parse tree produced by PapeteParser#FactTrue.
    def enterFactTrue(self, ctx:PapeteParser.FactTrueContext):
        pass

    # Exit a parse tree produced by PapeteParser#FactTrue.
    def exitFactTrue(self, ctx:PapeteParser.FactTrueContext):
        pass


    # Enter a parse tree produced by PapeteParser#FactFalse.
    def enterFactFalse(self, ctx:PapeteParser.FactFalseContext):
        pass

    # Exit a parse tree produced by PapeteParser#FactFalse.
    def exitFactFalse(self, ctx:PapeteParser.FactFalseContext):
        pass


    # Enter a parse tree produced by PapeteParser#FactCall.
    def enterFactCall(self, ctx:PapeteParser.FactCallContext):
        pass

    # Exit a parse tree produced by PapeteParser#FactCall.
    def exitFactCall(self, ctx:PapeteParser.FactCallContext):
        pass


    # Enter a parse tree produced by PapeteParser#FactExprBlock.
    def enterFactExprBlock(self, ctx:PapeteParser.FactExprBlockContext):
        pass

    # Exit a parse tree produced by PapeteParser#FactExprBlock.
    def exitFactExprBlock(self, ctx:PapeteParser.FactExprBlockContext):
        pass


    # Enter a parse tree produced by PapeteParser#OperationPlus.
    def enterOperationPlus(self, ctx:PapeteParser.OperationPlusContext):
        pass

    # Exit a parse tree produced by PapeteParser#OperationPlus.
    def exitOperationPlus(self, ctx:PapeteParser.OperationPlusContext):
        pass


    # Enter a parse tree produced by PapeteParser#OperationMinus.
    def enterOperationMinus(self, ctx:PapeteParser.OperationMinusContext):
        pass

    # Exit a parse tree produced by PapeteParser#OperationMinus.
    def exitOperationMinus(self, ctx:PapeteParser.OperationMinusContext):
        pass


    # Enter a parse tree produced by PapeteParser#OperationTimes.
    def enterOperationTimes(self, ctx:PapeteParser.OperationTimesContext):
        pass

    # Exit a parse tree produced by PapeteParser#OperationTimes.
    def exitOperationTimes(self, ctx:PapeteParser.OperationTimesContext):
        pass


    # Enter a parse tree produced by PapeteParser#OperationDiv.
    def enterOperationDiv(self, ctx:PapeteParser.OperationDivContext):
        pass

    # Exit a parse tree produced by PapeteParser#OperationDiv.
    def exitOperationDiv(self, ctx:PapeteParser.OperationDivContext):
        pass


    # Enter a parse tree produced by PapeteParser#OperationMod.
    def enterOperationMod(self, ctx:PapeteParser.OperationModContext):
        pass

    # Exit a parse tree produced by PapeteParser#OperationMod.
    def exitOperationMod(self, ctx:PapeteParser.OperationModContext):
        pass


    # Enter a parse tree produced by PapeteParser#OperationEe.
    def enterOperationEe(self, ctx:PapeteParser.OperationEeContext):
        pass

    # Exit a parse tree produced by PapeteParser#OperationEe.
    def exitOperationEe(self, ctx:PapeteParser.OperationEeContext):
        pass


    # Enter a parse tree produced by PapeteParser#OperationNe.
    def enterOperationNe(self, ctx:PapeteParser.OperationNeContext):
        pass

    # Exit a parse tree produced by PapeteParser#OperationNe.
    def exitOperationNe(self, ctx:PapeteParser.OperationNeContext):
        pass


    # Enter a parse tree produced by PapeteParser#OperationGt.
    def enterOperationGt(self, ctx:PapeteParser.OperationGtContext):
        pass

    # Exit a parse tree produced by PapeteParser#OperationGt.
    def exitOperationGt(self, ctx:PapeteParser.OperationGtContext):
        pass


    # Enter a parse tree produced by PapeteParser#OperationGe.
    def enterOperationGe(self, ctx:PapeteParser.OperationGeContext):
        pass

    # Exit a parse tree produced by PapeteParser#OperationGe.
    def exitOperationGe(self, ctx:PapeteParser.OperationGeContext):
        pass


    # Enter a parse tree produced by PapeteParser#OperationLt.
    def enterOperationLt(self, ctx:PapeteParser.OperationLtContext):
        pass

    # Exit a parse tree produced by PapeteParser#OperationLt.
    def exitOperationLt(self, ctx:PapeteParser.OperationLtContext):
        pass


    # Enter a parse tree produced by PapeteParser#OperationLe.
    def enterOperationLe(self, ctx:PapeteParser.OperationLeContext):
        pass

    # Exit a parse tree produced by PapeteParser#OperationLe.
    def exitOperationLe(self, ctx:PapeteParser.OperationLeContext):
        pass


    # Enter a parse tree produced by PapeteParser#OperationAnd.
    def enterOperationAnd(self, ctx:PapeteParser.OperationAndContext):
        pass

    # Exit a parse tree produced by PapeteParser#OperationAnd.
    def exitOperationAnd(self, ctx:PapeteParser.OperationAndContext):
        pass


    # Enter a parse tree produced by PapeteParser#OperationOr.
    def enterOperationOr(self, ctx:PapeteParser.OperationOrContext):
        pass

    # Exit a parse tree produced by PapeteParser#OperationOr.
    def exitOperationOr(self, ctx:PapeteParser.OperationOrContext):
        pass


    # Enter a parse tree produced by PapeteParser#TypeInt.
    def enterTypeInt(self, ctx:PapeteParser.TypeIntContext):
        pass

    # Exit a parse tree produced by PapeteParser#TypeInt.
    def exitTypeInt(self, ctx:PapeteParser.TypeIntContext):
        pass


    # Enter a parse tree produced by PapeteParser#TypeDouble.
    def enterTypeDouble(self, ctx:PapeteParser.TypeDoubleContext):
        pass

    # Exit a parse tree produced by PapeteParser#TypeDouble.
    def exitTypeDouble(self, ctx:PapeteParser.TypeDoubleContext):
        pass


    # Enter a parse tree produced by PapeteParser#TypeString.
    def enterTypeString(self, ctx:PapeteParser.TypeStringContext):
        pass

    # Exit a parse tree produced by PapeteParser#TypeString.
    def exitTypeString(self, ctx:PapeteParser.TypeStringContext):
        pass


    # Enter a parse tree produced by PapeteParser#TypeBool.
    def enterTypeBool(self, ctx:PapeteParser.TypeBoolContext):
        pass

    # Exit a parse tree produced by PapeteParser#TypeBool.
    def exitTypeBool(self, ctx:PapeteParser.TypeBoolContext):
        pass


    # Enter a parse tree produced by PapeteParser#TypeVoid.
    def enterTypeVoid(self, ctx:PapeteParser.TypeVoidContext):
        pass

    # Exit a parse tree produced by PapeteParser#TypeVoid.
    def exitTypeVoid(self, ctx:PapeteParser.TypeVoidContext):
        pass


    # Enter a parse tree produced by PapeteParser#TypeChar.
    def enterTypeChar(self, ctx:PapeteParser.TypeCharContext):
        pass

    # Exit a parse tree produced by PapeteParser#TypeChar.
    def exitTypeChar(self, ctx:PapeteParser.TypeCharContext):
        pass



# Generated from Grammar/Papete.g4 by ANTLR 4.7.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .PapeteParser import PapeteParser
else:
    from PapeteParser import PapeteParser

# This class defines a complete listener for a parse tree produced by PapeteParser.
class PapeteListener(ParseTreeListener):

    # Enter a parse tree produced by PapeteParser#prog.
    def enterProg(self, ctx:PapeteParser.ProgContext):
        pass

    # Exit a parse tree produced by PapeteParser#prog.
    def exitProg(self, ctx:PapeteParser.ProgContext):
        pass


    # Enter a parse tree produced by PapeteParser#AtrLine.
    def enterAtrLine(self, ctx:PapeteParser.AtrLineContext):
        pass

    # Exit a parse tree produced by PapeteParser#AtrLine.
    def exitAtrLine(self, ctx:PapeteParser.AtrLineContext):
        pass


    # Enter a parse tree produced by PapeteParser#PrintLine.
    def enterPrintLine(self, ctx:PapeteParser.PrintLineContext):
        pass

    # Exit a parse tree produced by PapeteParser#PrintLine.
    def exitPrintLine(self, ctx:PapeteParser.PrintLineContext):
        pass


    # Enter a parse tree produced by PapeteParser#InitLine.
    def enterInitLine(self, ctx:PapeteParser.InitLineContext):
        pass

    # Exit a parse tree produced by PapeteParser#InitLine.
    def exitInitLine(self, ctx:PapeteParser.InitLineContext):
        pass


    # Enter a parse tree produced by PapeteParser#CallFuncLine.
    def enterCallFuncLine(self, ctx:PapeteParser.CallFuncLineContext):
        pass

    # Exit a parse tree produced by PapeteParser#CallFuncLine.
    def exitCallFuncLine(self, ctx:PapeteParser.CallFuncLineContext):
        pass


    # Enter a parse tree produced by PapeteParser#func.
    def enterFunc(self, ctx:PapeteParser.FuncContext):
        pass

    # Exit a parse tree produced by PapeteParser#func.
    def exitFunc(self, ctx:PapeteParser.FuncContext):
        pass


    # Enter a parse tree produced by PapeteParser#AtrCmd.
    def enterAtrCmd(self, ctx:PapeteParser.AtrCmdContext):
        pass

    # Exit a parse tree produced by PapeteParser#AtrCmd.
    def exitAtrCmd(self, ctx:PapeteParser.AtrCmdContext):
        pass


    # Enter a parse tree produced by PapeteParser#InitCmd.
    def enterInitCmd(self, ctx:PapeteParser.InitCmdContext):
        pass

    # Exit a parse tree produced by PapeteParser#InitCmd.
    def exitInitCmd(self, ctx:PapeteParser.InitCmdContext):
        pass


    # Enter a parse tree produced by PapeteParser#PrintCmd.
    def enterPrintCmd(self, ctx:PapeteParser.PrintCmdContext):
        pass

    # Exit a parse tree produced by PapeteParser#PrintCmd.
    def exitPrintCmd(self, ctx:PapeteParser.PrintCmdContext):
        pass


    # Enter a parse tree produced by PapeteParser#ReadCmd.
    def enterReadCmd(self, ctx:PapeteParser.ReadCmdContext):
        pass

    # Exit a parse tree produced by PapeteParser#ReadCmd.
    def exitReadCmd(self, ctx:PapeteParser.ReadCmdContext):
        pass


    # Enter a parse tree produced by PapeteParser#IfCmd.
    def enterIfCmd(self, ctx:PapeteParser.IfCmdContext):
        pass

    # Exit a parse tree produced by PapeteParser#IfCmd.
    def exitIfCmd(self, ctx:PapeteParser.IfCmdContext):
        pass


    # Enter a parse tree produced by PapeteParser#WhileCmd.
    def enterWhileCmd(self, ctx:PapeteParser.WhileCmdContext):
        pass

    # Exit a parse tree produced by PapeteParser#WhileCmd.
    def exitWhileCmd(self, ctx:PapeteParser.WhileCmdContext):
        pass


    # Enter a parse tree produced by PapeteParser#ForCmd.
    def enterForCmd(self, ctx:PapeteParser.ForCmdContext):
        pass

    # Exit a parse tree produced by PapeteParser#ForCmd.
    def exitForCmd(self, ctx:PapeteParser.ForCmdContext):
        pass


    # Enter a parse tree produced by PapeteParser#FuncCmd.
    def enterFuncCmd(self, ctx:PapeteParser.FuncCmdContext):
        pass

    # Exit a parse tree produced by PapeteParser#FuncCmd.
    def exitFuncCmd(self, ctx:PapeteParser.FuncCmdContext):
        pass


    # Enter a parse tree produced by PapeteParser#callfunc.
    def enterCallfunc(self, ctx:PapeteParser.CallfuncContext):
        pass

    # Exit a parse tree produced by PapeteParser#callfunc.
    def exitCallfunc(self, ctx:PapeteParser.CallfuncContext):
        pass


    # Enter a parse tree produced by PapeteParser#while_.
    def enterWhile_(self, ctx:PapeteParser.While_Context):
        pass

    # Exit a parse tree produced by PapeteParser#while_.
    def exitWhile_(self, ctx:PapeteParser.While_Context):
        pass


    # Enter a parse tree produced by PapeteParser#for_.
    def enterFor_(self, ctx:PapeteParser.For_Context):
        pass

    # Exit a parse tree produced by PapeteParser#for_.
    def exitFor_(self, ctx:PapeteParser.For_Context):
        pass


    # Enter a parse tree produced by PapeteParser#NormalIfStmt.
    def enterNormalIfStmt(self, ctx:PapeteParser.NormalIfStmtContext):
        pass

    # Exit a parse tree produced by PapeteParser#NormalIfStmt.
    def exitNormalIfStmt(self, ctx:PapeteParser.NormalIfStmtContext):
        pass


    # Enter a parse tree produced by PapeteParser#NegIfStmt.
    def enterNegIfStmt(self, ctx:PapeteParser.NegIfStmtContext):
        pass

    # Exit a parse tree produced by PapeteParser#NegIfStmt.
    def exitNegIfStmt(self, ctx:PapeteParser.NegIfStmtContext):
        pass


    # Enter a parse tree produced by PapeteParser#IfElseIfStmt.
    def enterIfElseIfStmt(self, ctx:PapeteParser.IfElseIfStmtContext):
        pass

    # Exit a parse tree produced by PapeteParser#IfElseIfStmt.
    def exitIfElseIfStmt(self, ctx:PapeteParser.IfElseIfStmtContext):
        pass


    # Enter a parse tree produced by PapeteParser#OrCond.
    def enterOrCond(self, ctx:PapeteParser.OrCondContext):
        pass

    # Exit a parse tree produced by PapeteParser#OrCond.
    def exitOrCond(self, ctx:PapeteParser.OrCondContext):
        pass


    # Enter a parse tree produced by PapeteParser#CdandCond.
    def enterCdandCond(self, ctx:PapeteParser.CdandCondContext):
        pass

    # Exit a parse tree produced by PapeteParser#CdandCond.
    def exitCdandCond(self, ctx:PapeteParser.CdandCondContext):
        pass


    # Enter a parse tree produced by PapeteParser#AndCdand.
    def enterAndCdand(self, ctx:PapeteParser.AndCdandContext):
        pass

    # Exit a parse tree produced by PapeteParser#AndCdand.
    def exitAndCdand(self, ctx:PapeteParser.AndCdandContext):
        pass


    # Enter a parse tree produced by PapeteParser#CndtsCdand.
    def enterCndtsCdand(self, ctx:PapeteParser.CndtsCdandContext):
        pass

    # Exit a parse tree produced by PapeteParser#CndtsCdand.
    def exitCndtsCdand(self, ctx:PapeteParser.CndtsCdandContext):
        pass


    # Enter a parse tree produced by PapeteParser#RelopCndts.
    def enterRelopCndts(self, ctx:PapeteParser.RelopCndtsContext):
        pass

    # Exit a parse tree produced by PapeteParser#RelopCndts.
    def exitRelopCndts(self, ctx:PapeteParser.RelopCndtsContext):
        pass


    # Enter a parse tree produced by PapeteParser#CondCndts.
    def enterCondCndts(self, ctx:PapeteParser.CondCndtsContext):
        pass

    # Exit a parse tree produced by PapeteParser#CondCndts.
    def exitCondCndts(self, ctx:PapeteParser.CondCndtsContext):
        pass


    # Enter a parse tree produced by PapeteParser#relop.
    def enterRelop(self, ctx:PapeteParser.RelopContext):
        pass

    # Exit a parse tree produced by PapeteParser#relop.
    def exitRelop(self, ctx:PapeteParser.RelopContext):
        pass


    # Enter a parse tree produced by PapeteParser#read.
    def enterRead(self, ctx:PapeteParser.ReadContext):
        pass

    # Exit a parse tree produced by PapeteParser#read.
    def exitRead(self, ctx:PapeteParser.ReadContext):
        pass


    # Enter a parse tree produced by PapeteParser#ConcatPrint.
    def enterConcatPrint(self, ctx:PapeteParser.ConcatPrintContext):
        pass

    # Exit a parse tree produced by PapeteParser#ConcatPrint.
    def exitConcatPrint(self, ctx:PapeteParser.ConcatPrintContext):
        pass


    # Enter a parse tree produced by PapeteParser#VarPrint.
    def enterVarPrint(self, ctx:PapeteParser.VarPrintContext):
        pass

    # Exit a parse tree produced by PapeteParser#VarPrint.
    def exitVarPrint(self, ctx:PapeteParser.VarPrintContext):
        pass


    # Enter a parse tree produced by PapeteParser#init_.
    def enterInit_(self, ctx:PapeteParser.Init_Context):
        pass

    # Exit a parse tree produced by PapeteParser#init_.
    def exitInit_(self, ctx:PapeteParser.Init_Context):
        pass


    # Enter a parse tree produced by PapeteParser#VarRetr.
    def enterVarRetr(self, ctx:PapeteParser.VarRetrContext):
        pass

    # Exit a parse tree produced by PapeteParser#VarRetr.
    def exitVarRetr(self, ctx:PapeteParser.VarRetrContext):
        pass


    # Enter a parse tree produced by PapeteParser#ExprRetr.
    def enterExprRetr(self, ctx:PapeteParser.ExprRetrContext):
        pass

    # Exit a parse tree produced by PapeteParser#ExprRetr.
    def exitExprRetr(self, ctx:PapeteParser.ExprRetrContext):
        pass


    # Enter a parse tree produced by PapeteParser#IntAtr.
    def enterIntAtr(self, ctx:PapeteParser.IntAtrContext):
        pass

    # Exit a parse tree produced by PapeteParser#IntAtr.
    def exitIntAtr(self, ctx:PapeteParser.IntAtrContext):
        pass


    # Enter a parse tree produced by PapeteParser#DoubleAtr.
    def enterDoubleAtr(self, ctx:PapeteParser.DoubleAtrContext):
        pass

    # Exit a parse tree produced by PapeteParser#DoubleAtr.
    def exitDoubleAtr(self, ctx:PapeteParser.DoubleAtrContext):
        pass


    # Enter a parse tree produced by PapeteParser#StringAtr.
    def enterStringAtr(self, ctx:PapeteParser.StringAtrContext):
        pass

    # Exit a parse tree produced by PapeteParser#StringAtr.
    def exitStringAtr(self, ctx:PapeteParser.StringAtrContext):
        pass


    # Enter a parse tree produced by PapeteParser#BoolAtr.
    def enterBoolAtr(self, ctx:PapeteParser.BoolAtrContext):
        pass

    # Exit a parse tree produced by PapeteParser#BoolAtr.
    def exitBoolAtr(self, ctx:PapeteParser.BoolAtrContext):
        pass


    # Enter a parse tree produced by PapeteParser#VarExprFuncAtr.
    def enterVarExprFuncAtr(self, ctx:PapeteParser.VarExprFuncAtrContext):
        pass

    # Exit a parse tree produced by PapeteParser#VarExprFuncAtr.
    def exitVarExprFuncAtr(self, ctx:PapeteParser.VarExprFuncAtrContext):
        pass


    # Enter a parse tree produced by PapeteParser#VarStrAtr.
    def enterVarStrAtr(self, ctx:PapeteParser.VarStrAtrContext):
        pass

    # Exit a parse tree produced by PapeteParser#VarStrAtr.
    def exitVarStrAtr(self, ctx:PapeteParser.VarStrAtrContext):
        pass


    # Enter a parse tree produced by PapeteParser#VarBoolAtr.
    def enterVarBoolAtr(self, ctx:PapeteParser.VarBoolAtrContext):
        pass

    # Exit a parse tree produced by PapeteParser#VarBoolAtr.
    def exitVarBoolAtr(self, ctx:PapeteParser.VarBoolAtrContext):
        pass


    # Enter a parse tree produced by PapeteParser#TermExpr.
    def enterTermExpr(self, ctx:PapeteParser.TermExprContext):
        pass

    # Exit a parse tree produced by PapeteParser#TermExpr.
    def exitTermExpr(self, ctx:PapeteParser.TermExprContext):
        pass


    # Enter a parse tree produced by PapeteParser#SumExpr.
    def enterSumExpr(self, ctx:PapeteParser.SumExprContext):
        pass

    # Exit a parse tree produced by PapeteParser#SumExpr.
    def exitSumExpr(self, ctx:PapeteParser.SumExprContext):
        pass


    # Enter a parse tree produced by PapeteParser#MinusExpr.
    def enterMinusExpr(self, ctx:PapeteParser.MinusExprContext):
        pass

    # Exit a parse tree produced by PapeteParser#MinusExpr.
    def exitMinusExpr(self, ctx:PapeteParser.MinusExprContext):
        pass


    # Enter a parse tree produced by PapeteParser#FactTerm.
    def enterFactTerm(self, ctx:PapeteParser.FactTermContext):
        pass

    # Exit a parse tree produced by PapeteParser#FactTerm.
    def exitFactTerm(self, ctx:PapeteParser.FactTermContext):
        pass


    # Enter a parse tree produced by PapeteParser#MultTerm.
    def enterMultTerm(self, ctx:PapeteParser.MultTermContext):
        pass

    # Exit a parse tree produced by PapeteParser#MultTerm.
    def exitMultTerm(self, ctx:PapeteParser.MultTermContext):
        pass


    # Enter a parse tree produced by PapeteParser#DivTerm.
    def enterDivTerm(self, ctx:PapeteParser.DivTermContext):
        pass

    # Exit a parse tree produced by PapeteParser#DivTerm.
    def exitDivTerm(self, ctx:PapeteParser.DivTermContext):
        pass


    # Enter a parse tree produced by PapeteParser#RestTerm.
    def enterRestTerm(self, ctx:PapeteParser.RestTermContext):
        pass

    # Exit a parse tree produced by PapeteParser#RestTerm.
    def exitRestTerm(self, ctx:PapeteParser.RestTermContext):
        pass


    # Enter a parse tree produced by PapeteParser#varFact.
    def enterVarFact(self, ctx:PapeteParser.VarFactContext):
        pass

    # Exit a parse tree produced by PapeteParser#varFact.
    def exitVarFact(self, ctx:PapeteParser.VarFactContext):
        pass


    # Enter a parse tree produced by PapeteParser#NumDoubleFact.
    def enterNumDoubleFact(self, ctx:PapeteParser.NumDoubleFactContext):
        pass

    # Exit a parse tree produced by PapeteParser#NumDoubleFact.
    def exitNumDoubleFact(self, ctx:PapeteParser.NumDoubleFactContext):
        pass


    # Enter a parse tree produced by PapeteParser#NumIntFact.
    def enterNumIntFact(self, ctx:PapeteParser.NumIntFactContext):
        pass

    # Exit a parse tree produced by PapeteParser#NumIntFact.
    def exitNumIntFact(self, ctx:PapeteParser.NumIntFactContext):
        pass


    # Enter a parse tree produced by PapeteParser#exprFact.
    def enterExprFact(self, ctx:PapeteParser.ExprFactContext):
        pass

    # Exit a parse tree produced by PapeteParser#exprFact.
    def exitExprFact(self, ctx:PapeteParser.ExprFactContext):
        pass


    # Enter a parse tree produced by PapeteParser#intType.
    def enterIntType(self, ctx:PapeteParser.IntTypeContext):
        pass

    # Exit a parse tree produced by PapeteParser#intType.
    def exitIntType(self, ctx:PapeteParser.IntTypeContext):
        pass


    # Enter a parse tree produced by PapeteParser#doubleType.
    def enterDoubleType(self, ctx:PapeteParser.DoubleTypeContext):
        pass

    # Exit a parse tree produced by PapeteParser#doubleType.
    def exitDoubleType(self, ctx:PapeteParser.DoubleTypeContext):
        pass


    # Enter a parse tree produced by PapeteParser#floatType.
    def enterFloatType(self, ctx:PapeteParser.FloatTypeContext):
        pass

    # Exit a parse tree produced by PapeteParser#floatType.
    def exitFloatType(self, ctx:PapeteParser.FloatTypeContext):
        pass


    # Enter a parse tree produced by PapeteParser#stringType.
    def enterStringType(self, ctx:PapeteParser.StringTypeContext):
        pass

    # Exit a parse tree produced by PapeteParser#stringType.
    def exitStringType(self, ctx:PapeteParser.StringTypeContext):
        pass


    # Enter a parse tree produced by PapeteParser#boolType.
    def enterBoolType(self, ctx:PapeteParser.BoolTypeContext):
        pass

    # Exit a parse tree produced by PapeteParser#boolType.
    def exitBoolType(self, ctx:PapeteParser.BoolTypeContext):
        pass



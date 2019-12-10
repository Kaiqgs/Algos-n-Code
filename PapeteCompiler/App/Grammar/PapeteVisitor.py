# Generated from App/Grammar/Papete.g4 by ANTLR 4.7.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .PapeteParser import PapeteParser
else:
    from PapeteParser import PapeteParser

# This class defines a complete generic visitor for a parse tree produced by PapeteParser.

class PapeteVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by PapeteParser#prog.
    def visitProg(self, ctx:PapeteParser.ProgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PapeteParser#line.
    def visitLine(self, ctx:PapeteParser.LineContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PapeteParser#assg.
    def visitAssg(self, ctx:PapeteParser.AssgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PapeteParser#decl.
    def visitDecl(self, ctx:PapeteParser.DeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PapeteParser#expr.
    def visitExpr(self, ctx:PapeteParser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PapeteParser#funcsign.
    def visitFuncsign(self, ctx:PapeteParser.FuncsignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PapeteParser#stmt.
    def visitStmt(self, ctx:PapeteParser.StmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PapeteParser#fact.
    def visitFact(self, ctx:PapeteParser.FactContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PapeteParser#type_.
    def visitType_(self, ctx:PapeteParser.Type_Context):
        return self.visitChildren(ctx)



del PapeteParser
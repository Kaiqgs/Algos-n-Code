# Generated from App/Grammar/Papete.g4 by ANTLR 4.7.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\30")
        buf.write("c\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\4\t\t\t\4\n\t\n\3\2\3\2\3\2\7\2\30\n\2\f\2\16\2\33")
        buf.write("\13\2\3\2\3\2\3\3\3\3\3\4\3\4\3\4\3\4\3\5\3\5\3\5\3\6")
        buf.write("\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3")
        buf.write("\6\3\6\3\6\3\6\7\6:\n\6\f\6\16\6=\13\6\3\7\3\7\3\7\3\7")
        buf.write("\7\7C\n\7\f\7\16\7F\13\7\3\7\3\7\3\7\3\b\3\b\3\b\3\b\7")
        buf.write("\bO\n\b\f\b\16\bR\13\b\3\b\3\b\3\t\3\t\3\t\3\t\3\t\3\t")
        buf.write("\3\t\3\t\3\t\5\t_\n\t\3\n\3\n\3\n\2\3\n\13\2\4\6\b\n\f")
        buf.write("\16\20\22\2\3\3\2\13\16\2f\2\31\3\2\2\2\4\36\3\2\2\2\6")
        buf.write(" \3\2\2\2\b$\3\2\2\2\n\'\3\2\2\2\f>\3\2\2\2\16J\3\2\2")
        buf.write("\2\20^\3\2\2\2\22`\3\2\2\2\24\25\5\4\3\2\25\26\7\23\2")
        buf.write("\2\26\30\3\2\2\2\27\24\3\2\2\2\30\33\3\2\2\2\31\27\3\2")
        buf.write("\2\2\31\32\3\2\2\2\32\34\3\2\2\2\33\31\3\2\2\2\34\35\7")
        buf.write("\2\2\3\35\3\3\2\2\2\36\37\5\6\4\2\37\5\3\2\2\2 !\5\b\5")
        buf.write("\2!\"\7\3\2\2\"#\5\n\6\2#\7\3\2\2\2$%\5\22\n\2%&\7\25")
        buf.write("\2\2&\t\3\2\2\2\'(\b\6\1\2()\5\20\t\2);\3\2\2\2*+\f\7")
        buf.write("\2\2+,\7\4\2\2,:\5\20\t\2-.\f\6\2\2./\7\5\2\2/:\5\20\t")
        buf.write("\2\60\61\f\5\2\2\61\62\7\6\2\2\62:\5\20\t\2\63\64\f\4")
        buf.write("\2\2\64\65\7\7\2\2\65:\5\20\t\2\66\67\f\3\2\2\678\7\b")
        buf.write("\2\28:\5\20\t\29*\3\2\2\29-\3\2\2\29\60\3\2\2\29\63\3")
        buf.write("\2\2\29\66\3\2\2\2:=\3\2\2\2;9\3\2\2\2;<\3\2\2\2<\13\3")
        buf.write("\2\2\2=;\3\2\2\2>?\5\22\n\2?@\7\25\2\2@D\7\17\2\2AC\5")
        buf.write("\b\5\2BA\3\2\2\2CF\3\2\2\2DB\3\2\2\2DE\3\2\2\2EG\3\2\2")
        buf.write("\2FD\3\2\2\2GH\7\20\2\2HI\5\16\b\2I\r\3\2\2\2JP\7\21\2")
        buf.write("\2KL\5\4\3\2LM\7\23\2\2MO\3\2\2\2NK\3\2\2\2OR\3\2\2\2")
        buf.write("PN\3\2\2\2PQ\3\2\2\2QS\3\2\2\2RP\3\2\2\2ST\7\2\2\3T\17")
        buf.write("\3\2\2\2U_\7\25\2\2V_\7\26\2\2W_\7\24\2\2X_\7\t\2\2Y_")
        buf.write("\7\n\2\2Z[\7\17\2\2[\\\5\n\6\2\\]\7\20\2\2]_\3\2\2\2^")
        buf.write("U\3\2\2\2^V\3\2\2\2^W\3\2\2\2^X\3\2\2\2^Y\3\2\2\2^Z\3")
        buf.write("\2\2\2_\21\3\2\2\2`a\t\2\2\2a\23\3\2\2\2\b\319;DP^")
        return buf.getvalue()


class PapeteParser ( Parser ):

    grammarFileName = "Papete.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'='", "'+'", "'-'", "'*'", "'/'", "'%'", 
                     "'true'", "'false'", "'int'", "'double'", "'string'", 
                     "'bool'", "'('", "')'", "'{'", "'}'", "';'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "TRUE", "FALSE", 
                      "INT_TYPE", "FLOAT_TYPE", "STRING_TYPE", "BOOL_TYPE", 
                      "PAROPEN", "PARCLOSE", "BROPEN", "BRCLOSE", "EOL", 
                      "STRING", "VAR", "NUM", "DIGIT", "WS" ]

    RULE_prog = 0
    RULE_line = 1
    RULE_assg = 2
    RULE_decl = 3
    RULE_expr = 4
    RULE_funcsign = 5
    RULE_stmt = 6
    RULE_fact = 7
    RULE_type_ = 8

    ruleNames =  [ "prog", "line", "assg", "decl", "expr", "funcsign", "stmt", 
                   "fact", "type_" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    TRUE=7
    FALSE=8
    INT_TYPE=9
    FLOAT_TYPE=10
    STRING_TYPE=11
    BOOL_TYPE=12
    PAROPEN=13
    PARCLOSE=14
    BROPEN=15
    BRCLOSE=16
    EOL=17
    STRING=18
    VAR=19
    NUM=20
    DIGIT=21
    WS=22

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(PapeteParser.EOF, 0)

        def line(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PapeteParser.LineContext)
            else:
                return self.getTypedRuleContext(PapeteParser.LineContext,i)


        def EOL(self, i:int=None):
            if i is None:
                return self.getTokens(PapeteParser.EOL)
            else:
                return self.getToken(PapeteParser.EOL, i)

        def getRuleIndex(self):
            return PapeteParser.RULE_prog

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProg" ):
                listener.enterProg(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProg" ):
                listener.exitProg(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProg" ):
                return visitor.visitProg(self)
            else:
                return visitor.visitChildren(self)




    def prog(self):

        localctx = PapeteParser.ProgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_prog)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 23
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << PapeteParser.INT_TYPE) | (1 << PapeteParser.FLOAT_TYPE) | (1 << PapeteParser.STRING_TYPE) | (1 << PapeteParser.BOOL_TYPE))) != 0):
                self.state = 18
                self.line()
                self.state = 19
                self.match(PapeteParser.EOL)
                self.state = 25
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 26
            self.match(PapeteParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LineContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assg(self):
            return self.getTypedRuleContext(PapeteParser.AssgContext,0)


        def getRuleIndex(self):
            return PapeteParser.RULE_line

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLine" ):
                listener.enterLine(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLine" ):
                listener.exitLine(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLine" ):
                return visitor.visitLine(self)
            else:
                return visitor.visitChildren(self)




    def line(self):

        localctx = PapeteParser.LineContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_line)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 28
            self.assg()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssgContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def decl(self):
            return self.getTypedRuleContext(PapeteParser.DeclContext,0)


        def expr(self):
            return self.getTypedRuleContext(PapeteParser.ExprContext,0)


        def getRuleIndex(self):
            return PapeteParser.RULE_assg

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssg" ):
                listener.enterAssg(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssg" ):
                listener.exitAssg(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssg" ):
                return visitor.visitAssg(self)
            else:
                return visitor.visitChildren(self)




    def assg(self):

        localctx = PapeteParser.AssgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_assg)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 30
            self.decl()
            self.state = 31
            self.match(PapeteParser.T__0)

            self.state = 32
            self.expr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def type_(self):
            return self.getTypedRuleContext(PapeteParser.Type_Context,0)


        def VAR(self):
            return self.getToken(PapeteParser.VAR, 0)

        def getRuleIndex(self):
            return PapeteParser.RULE_decl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDecl" ):
                listener.enterDecl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDecl" ):
                listener.exitDecl(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDecl" ):
                return visitor.visitDecl(self)
            else:
                return visitor.visitChildren(self)




    def decl(self):

        localctx = PapeteParser.DeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_decl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 34
            self.type_()
            self.state = 35
            self.match(PapeteParser.VAR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def fact(self):
            return self.getTypedRuleContext(PapeteParser.FactContext,0)


        def expr(self):
            return self.getTypedRuleContext(PapeteParser.ExprContext,0)


        def getRuleIndex(self):
            return PapeteParser.RULE_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr" ):
                listener.enterExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr" ):
                listener.exitExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr" ):
                return visitor.visitExpr(self)
            else:
                return visitor.visitChildren(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = PapeteParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 8
        self.enterRecursionRule(localctx, 8, self.RULE_expr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 38
            self.fact()
            self._ctx.stop = self._input.LT(-1)
            self.state = 57
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,2,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 55
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
                    if la_ == 1:
                        localctx = PapeteParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 40
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 41
                        self.match(PapeteParser.T__1)
                        self.state = 42
                        self.fact()
                        pass

                    elif la_ == 2:
                        localctx = PapeteParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 43
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 44
                        self.match(PapeteParser.T__2)
                        self.state = 45
                        self.fact()
                        pass

                    elif la_ == 3:
                        localctx = PapeteParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 46
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 47
                        self.match(PapeteParser.T__3)
                        self.state = 48
                        self.fact()
                        pass

                    elif la_ == 4:
                        localctx = PapeteParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 49
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 50
                        self.match(PapeteParser.T__4)
                        self.state = 51
                        self.fact()
                        pass

                    elif la_ == 5:
                        localctx = PapeteParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 52
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 53
                        self.match(PapeteParser.T__5)
                        self.state = 54
                        self.fact()
                        pass

             
                self.state = 59
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,2,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class FuncsignContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def type_(self):
            return self.getTypedRuleContext(PapeteParser.Type_Context,0)


        def VAR(self):
            return self.getToken(PapeteParser.VAR, 0)

        def PAROPEN(self):
            return self.getToken(PapeteParser.PAROPEN, 0)

        def PARCLOSE(self):
            return self.getToken(PapeteParser.PARCLOSE, 0)

        def stmt(self):
            return self.getTypedRuleContext(PapeteParser.StmtContext,0)


        def decl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PapeteParser.DeclContext)
            else:
                return self.getTypedRuleContext(PapeteParser.DeclContext,i)


        def getRuleIndex(self):
            return PapeteParser.RULE_funcsign

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFuncsign" ):
                listener.enterFuncsign(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFuncsign" ):
                listener.exitFuncsign(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFuncsign" ):
                return visitor.visitFuncsign(self)
            else:
                return visitor.visitChildren(self)




    def funcsign(self):

        localctx = PapeteParser.FuncsignContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_funcsign)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 60
            self.type_()
            self.state = 61
            self.match(PapeteParser.VAR)
            self.state = 62
            self.match(PapeteParser.PAROPEN)
            self.state = 66
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << PapeteParser.INT_TYPE) | (1 << PapeteParser.FLOAT_TYPE) | (1 << PapeteParser.STRING_TYPE) | (1 << PapeteParser.BOOL_TYPE))) != 0):
                self.state = 63
                self.decl()
                self.state = 68
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 69
            self.match(PapeteParser.PARCLOSE)
            self.state = 70
            self.stmt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BROPEN(self):
            return self.getToken(PapeteParser.BROPEN, 0)

        def EOF(self):
            return self.getToken(PapeteParser.EOF, 0)

        def line(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PapeteParser.LineContext)
            else:
                return self.getTypedRuleContext(PapeteParser.LineContext,i)


        def EOL(self, i:int=None):
            if i is None:
                return self.getTokens(PapeteParser.EOL)
            else:
                return self.getToken(PapeteParser.EOL, i)

        def getRuleIndex(self):
            return PapeteParser.RULE_stmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStmt" ):
                listener.enterStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStmt" ):
                listener.exitStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmt" ):
                return visitor.visitStmt(self)
            else:
                return visitor.visitChildren(self)




    def stmt(self):

        localctx = PapeteParser.StmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 72
            self.match(PapeteParser.BROPEN)
            self.state = 78
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << PapeteParser.INT_TYPE) | (1 << PapeteParser.FLOAT_TYPE) | (1 << PapeteParser.STRING_TYPE) | (1 << PapeteParser.BOOL_TYPE))) != 0):
                self.state = 73
                self.line()
                self.state = 74
                self.match(PapeteParser.EOL)
                self.state = 80
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 81
            self.match(PapeteParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FactContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR(self):
            return self.getToken(PapeteParser.VAR, 0)

        def NUM(self):
            return self.getToken(PapeteParser.NUM, 0)

        def STRING(self):
            return self.getToken(PapeteParser.STRING, 0)

        def TRUE(self):
            return self.getToken(PapeteParser.TRUE, 0)

        def FALSE(self):
            return self.getToken(PapeteParser.FALSE, 0)

        def PAROPEN(self):
            return self.getToken(PapeteParser.PAROPEN, 0)

        def expr(self):
            return self.getTypedRuleContext(PapeteParser.ExprContext,0)


        def PARCLOSE(self):
            return self.getToken(PapeteParser.PARCLOSE, 0)

        def getRuleIndex(self):
            return PapeteParser.RULE_fact

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFact" ):
                listener.enterFact(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFact" ):
                listener.exitFact(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFact" ):
                return visitor.visitFact(self)
            else:
                return visitor.visitChildren(self)




    def fact(self):

        localctx = PapeteParser.FactContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_fact)
        try:
            self.state = 92
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [PapeteParser.VAR]:
                self.enterOuterAlt(localctx, 1)
                self.state = 83
                self.match(PapeteParser.VAR)
                pass
            elif token in [PapeteParser.NUM]:
                self.enterOuterAlt(localctx, 2)
                self.state = 84
                self.match(PapeteParser.NUM)
                pass
            elif token in [PapeteParser.STRING]:
                self.enterOuterAlt(localctx, 3)
                self.state = 85
                self.match(PapeteParser.STRING)
                pass
            elif token in [PapeteParser.TRUE]:
                self.enterOuterAlt(localctx, 4)
                self.state = 86
                self.match(PapeteParser.TRUE)
                pass
            elif token in [PapeteParser.FALSE]:
                self.enterOuterAlt(localctx, 5)
                self.state = 87
                self.match(PapeteParser.FALSE)
                pass
            elif token in [PapeteParser.PAROPEN]:
                self.enterOuterAlt(localctx, 6)
                self.state = 88
                self.match(PapeteParser.PAROPEN)
                self.state = 89
                self.expr(0)
                self.state = 90
                self.match(PapeteParser.PARCLOSE)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Type_Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT_TYPE(self):
            return self.getToken(PapeteParser.INT_TYPE, 0)

        def FLOAT_TYPE(self):
            return self.getToken(PapeteParser.FLOAT_TYPE, 0)

        def STRING_TYPE(self):
            return self.getToken(PapeteParser.STRING_TYPE, 0)

        def BOOL_TYPE(self):
            return self.getToken(PapeteParser.BOOL_TYPE, 0)

        def getRuleIndex(self):
            return PapeteParser.RULE_type_

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterType_" ):
                listener.enterType_(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitType_" ):
                listener.exitType_(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitType_" ):
                return visitor.visitType_(self)
            else:
                return visitor.visitChildren(self)




    def type_(self):

        localctx = PapeteParser.Type_Context(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_type_)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 94
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << PapeteParser.INT_TYPE) | (1 << PapeteParser.FLOAT_TYPE) | (1 << PapeteParser.STRING_TYPE) | (1 << PapeteParser.BOOL_TYPE))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[4] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 2)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 1)
         





# Review for midterm #1

The midterm covers all content through and including language V4.

* Sources relevant to study
  * Readings
    * Readings: https://ourplcc.github.io/course-materials-ng/dev/, up to V4
    * Assignments: a1-a3
    * Your personal notes up to V4
    * This review sheet
* Language specification
    * Lexical analysis
      * Lexer/scanner
      * Tokens
      * Lexemes
      * Token rules
      * Skip rules
      * Longest-first match rule
      * Regex
    * Syntactic analysis
      * Parser
      * Start symbol
      * Terminals
      * Non-terminals
      * BNF notation
      * Mapping rules to classes and attributes/instance variables
      * Naming LHS non-terminals to disambiguate
      * Naming RHS terminals and non-terminals to disambiguate
      * Repeating rules and optional separator
      * Parse tree/abstract parse tree/abstract syntax tree
      * Captured and not captured tokens
    * Semantic analysis
      * `plcc-rep`
        * Able to implement a polymorphic method across alternatives
        * `_run` method and the class for the start symbol
        * Able to read and write small snippets of code to walk a parse tree to
          accomplish some goal
* The V* language
  * `Env` - `EnvNode`, `EnvNull`, `Val`, `IntVal`
  * V0
    * Basic expressions: `LitExp`, `VarExp`, `PrimappExp`
    * Pretty print them with `__str__`
  * V1
    * Use `Env` to evaluate basic expressions
  * V2
    * `IfExp`
    * Truthiness of `Val`s.
  * V3
    * `LetExp`
  * V4
    * `ProcExp`, `AppExp`, `LetExp`-`AppExp`-identity, `SeqExp`
* Skills
  * Draw an environment diagram to show the environments created during the
    evaluation of given code in V4 and the environments a `ProcVal` captures
  * Determine the value of a program written in V4
  * Write a small program in V4
  * Rewrite a `LetExp` as an `AppExp`
  * Know and use PLCC commands: `plcc-scan`, `plcc-parse`, and `plcc-rep`
* Terminology
  * Closure
  * Static scoping
  * Free vs bound variables for a given `proc`

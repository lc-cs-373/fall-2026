# Programming Language Structures

## Course information

Lewis & Clark College, Fall 2026  
CS 373, Section 01  
Monday/Wednesday/Friday 1:50-2:50 AM  
Olin 305

**Google Classroom:** I will use Google Classroom throughout the semester to
share assignment due dates, to share details about exams, and to track your
grade.

**GitHub:** I will use GitHub to share assignments.

**Textbook:** No textbook for this class, instead we will use
[these](https://ourplcc.github.io/course-materials-ng/dev/) informal notes.

**Tool:** Demonstrations, activities, and assignments will use
[PLCC](https://ourplcc.github.io/plcc-ng/2.0/), a compiler compiler, along
with a preexisting set of
[languages](https://github.com/ourPLCC/languages-ng/tree/v1.0.0) implemented
using PLCC.

## Teacher information

Professor: Alain Kägi  
Pronouns: He/him  
Email: alaink@lclark.edu  
Office hours:
* Mondays & Wednesdays 12:00 - 1 PM, Olin 226B
* Thursdays 1 - 3 PM, Olin 226B

## Course description

In this course, you will learn fundamental concepts related to the design and
implementation of programming languages. We will dive into lexical, syntactic,
and semantic analysis. We will study different programming paradigms, including
functional, procedural, and object-oriented. We will pay special attention
various call semantics, the difference between dynamic vs. static scoping, and
type systems.

## Course goals

My primary goal is to help you master some important concepts of programming
languages such as syntax analysis, scoping rules, function call semantics, and
type systems.

Through the assignments, you will also gain some experience reading and
extending object-oriented programs.

Programming assignments will be done in Python.

## Learning outcomes

The learning objectives for this class include:

1. Develop simple regular expressions to match patterns in text.
2. Analyze language syntax using context-free grammars and Backus-Naur Form
   (BNF) to construct abstract syntax trees.
3. Trace program execution using environments and scoping rules.
4. Implement type checking algorithms for static type systems.
5. Contrast evaluation strategies such as call-by-value, call-by-reference,
   call-by-name, and lazy evaluation.
6. Implement the framework to support first-class and higher-order functions.
7. Map object-oriented mechanisms (dynamic dispatch, inheritance, static vs.
   instance members) to their underlying procedural and functional
   representations.
8. Construct an interpreter or domain-specific language (DSL) using a parser
   generator and environment-based evaluation.

## Office hours

I hope you will visit me throughout the term, so I can learn more about your
interests and answer your questions. No appointment is necessary to see me
during office hours; simply stop by Olin 226B for in-person office hours
(Mondays/Wednesdays 12:00 - 1 PM and Thursdays 1 - 3 PM). If you would like to
make an appointment outside of my office hours, please email me at
alaink@lclark.edu.

## Requirements

All assignments will be posted on GitHub and will be submitted through Google
Classroom. They are designed to help you master and apply what we are learning
in class. **Assignments are due on Friday at 11:59 PM of the week they are
due.** Points will be taken off if submitted late; in some cases late
assignments will not receive any credit.

## Grade scale

I will use the following scale to compute your final grade:

Grade            | Point Range
-|-
**A− or A**      | 90-100
**B−, B, or B+** | 80-89
**C or C+**      | 72-79
**C−**           | 70-71
**D+**           | 68-69
**D**            | 62-67
**F**            |  0-61

Note that I may adjust your final grade in the class up or down in light of your
participation, attendance, and overall commitment to the class.

## Grading

* Assignments: 25%
* Midterm exam 1: 25%
* Midterm exam 2: 25%
* Final exam: 25%

Assignments are 25% of your grade and considerably more than 25% of your
learning. That weight is deliberate. An assignment grade cannot tell me whether
you did the work or whether something did it for you, so I have assigned weights
where I can actually see what you know. Do an assignment for what it teaches
you, not for what it is worth.

**Replacement rule.** If your score on the final exam is higher than your score
on your lower midterm, that midterm score is replaced by your final exam score.
This substitution happens automatically and you do not need to request it. The
material in this course builds, so demonstrating late in the term that you have
mastered earlier material counts for something. This policy applies only to
exams you have taken; a missed exam is governed by the Attendance Policy.

## Helpful tips

**Attend all class meetings.** The classroom is a place to learn new concepts,
to work through activities to reinforce learning, and to engage in discussions
with your professors and your peers. If you have to miss class for illness or
an emergency, please let me know and try to ask a peer to take notes for you.
Being on time for class is also important.

**Collaborate with your peers.** Form a study group and get together to talk
about the class. The sooner you get together with your peers to talk about the
class, the better. That way you can look over your notes right away, when they
are still fresh. You are likely to learn a lot from one another and find places
where you need clarification from me before exam-time. You may collaborate on
assignments, but you need to develop your own answers.

**Divide and conquer — split up some of the exam review.** When it comes time to
review and to prepare for exams, you will have another great opportunity for
collaboration. Split up readings and lectures among a group of people and have
each person prepare parts of the study guides and potential answers to exam
questions. Then trade study guides and get together for your own review
sessions.

**Get to know your professor.** Please feel free to stop by my office hours
early in the semester, and stop by often. I am here not only to answer questions
about the lectures and the assignments, but also to engage in conversation about
topics beyond computer science.

## Tentative schedule

**W** | **Monday**         | **Wednesday**      | **Friday**         | **Due**
-|-|-|-|-
 1    | Syllabus, setup    | *No Class*         | Tokens and PLCC    |
 2    | *No Class*         | Syntactic Analysis | Semantic Analysis  | **A1**
 3    | V0                 | Environments       | V1                 |
 4    | V2                 | V3                 | V4                 | **A2**
 5    | V5                 | V6                 | Variables          |
 6    | Side effects       |                    | *No Class*         | **A3**
 7    | Exam 1 Review      | **Exam 1**         |                    |
 8    | SET                | REF                | NAME               | **A4**
 9    |                    |                    | TYPE0              |
10    | TYPE1              | TYPE1 (cont'd)     | TYPE1 (cont'd)     | **A5**
11    | Exam 2 Review      | **Exam 2**         |                    |
12    |                    |                    |                    | **A6**
13    | OBJ                | *No Class*         | *No Class*         |
14    | OBJ                | OBJ                |                    | **A7**
15    |                    | Review for final   | *No Class*         |

## Course policies

**Attendance.** Attendance is key to master the topics covered in this course.
Participation in discussion and activities will help gain that proficiency.
If you must miss a class for any reason, please obtain information about the
the missed class from your classmates. Missing an exam disadvantages not only
you but also your classmates and me. Make-up exams will only be given for
serious circumstances. In any event, if you will miss an exam, you must contact
me ***before*** the exam to schedule a makeup exam or alternate
assessment. Therefore, 

**Accommodations.** Please see me if there are accommodations that could help
you learn more effectively in this class or if you are experiencing barriers to
accessibility in our class. Some kinds of accommodations may require
documentation through the
[Office of Student Accessibility](https://www.lclark.edu/offices/student-accessibility/).
If you plan to take exams in the Office of Student Accessibility, please
schedule with them and let me know well in advance of the exam.

**Exams.** Exams assess your knowledge of concepts, terminology, and your
ability to reason about topics introduced in class. There are 2 midterm exams
and a final exam. Each exam covers the materials since the last exam. Exams are
closed-computer, closed-book, and closed-note.

**Assignments.** A homework assignment will be due about every other week.
Homework assignments provide you with an opportunity to apply and to deepen your
understanding of the course material. Discussing strategies and roadblocks with
your classmates is encouraged, and so is using AI in the ways described under
*AI and Your Learning*. The last homework assignment is graded for completeness
only, not for correctness. It carries the same weight as every other assignment.
Rather than returning individual feedback on it, I will release solutions before
the review session for the final exam, so you can check your own work while
preparing. A separate [document](./grading.md) describes how I grade
assignments.

**Late work policy.** Generally assignments are due on Friday of the week they
are due. You may complete an assignment up to 72 hours (3 days) after its due
date without penalty; so, the grace period typically ends on the following
Monday. Assignments will be accepted up to 1 week late, but correctness is not
checked and earns no credit — only completeness does. This caps a late
submission at roughly half credit. After one week late, work will not be
accepted and receives a 0.

**Course withdrawals.** You may drop this course on WebAdvisor by Friday of the
second week of class and no W grade will appear on your transcript. After the
second week and before 4 PM on Friday of the 10th week, you can withdraw from
the course by submitting a Course Withdrawal form to the Registrar’s Office. In
this case, a W grade will appear on your transcript. **The last day to withdraw
from this class is Friday, November 6th.** It is not possible for me to
authorize your withdrawal from the course after that date. At that point, you
will need to complete the course and take whatever grade you have earned. If
you have questions or concerns about your performance in the course, please talk
with me before **November 6th**.

**AI and your learning.** ***You may use AI tools on assignments. You may not
use them on exams.*** That is the whole rule. The difference between its two
halves matters more than it may appear. Assignments are the only chance you get
to work through these ideas yourself, at your own pace, with time to be confused
and to recover. Lecture cannot give you that, and an exam certainly cannot. An
AI that produces a finished assignment for you may genuinely save you work — but
it also wastes your one opportunity to learn the material. The practical
consequence arrives in December. Three quarters of your grade comes from exams
you take without help of any kind. Used differently, AI can genuinely help:
Explaining a concept a second way, getting you unstuck, generating extra
practice, quizzing you on material you think you already know. These uses are
encouraged. The library’s
[Generative Artificial Intelligence](https://library.lclark.edu/ai) is a
reasonable place to start if you want to use these tools well.

**Academic integrity.** Academic integrity is an essential part of learning.
Plagiarism, cheating, or the deliberate misrepresentation of information will
result in failure of this course. Please avoid any behavior that may be
reasonably viewed as suspicious. Remember that helping a classmate to cheat
counts as cheating. If you have any questions about the use of generative AI
technology or plagiarism boundaries or about what type of material you can
access while working on an assignment, please see me before you turn in your
work. If you have any questions or concerns about academic honesty, please come
see me or refer to Lewis & Clark’s
[Academic Integrity Policy](https://docs.lclark.edu/undergraduate/policiesprocedures/academicintegrity/).

**Other.** All college policies govern this course. Please see the
[Undergraduate Catalog](https://college.lclark.edu/catalog/) for any issues not
covered in this syllabus.

**Changes to this syllabus.** This syllabus and these policies are subject to
change as deemed necessary by the instructor. Changes to this document will be
announced in class and on Google classroom. A revised syllabus will be posted to
Google classroom and the GitHub class repository.

#VIOLIN SCALE GENERATOR
Randomly generates musical scales with bowings

To run:
$ python violin_scale_generator/violin_scale_generator.py

The aim of the application is to help violin students practice their scales by generating a random scale out of the user's set of scales and bowing patterns.

The program is currently able to:

- request username input (currently accepts users 'lilit', 'beginner', and 'test');
- call up that user's set of scales and bowings (the scales they are familiar with);
- generate a random scale (with bowing pattern) out of that set;
- if the user requests, the program will continue to generate scales until all scale/bowing variations have been generated, and then loop through again (randomly) until user stops requesting. 

Additional goals not yet achieved:

- allow user to use button to generate scale after scale, rather than typing reqponse to prompt in console;
- allow users to set up or edit their own scale/bowing sets (all currently done in the code by developer);
- distinguish user types: 
  (1) "teacher" - able to create and edit own and students' users/scale sets, and
  (2) "student" - only able to access own scale sets.

Bugs to fix:

- "None Type" errors

/* The chat const defines the Peekobot conversation.
 * 
 * It should be an object with numerical property names, and each property is an entry
 * in the conversation.
 * 
 * A conversation entry should have:
 *  - A "text" property that is what the chatbot says at this point in the conversation
 *  - Either:
 *     - A "next" property, which defines the next chat entry by stating a numerical key
 *       of the chat object and is used when the chatbot needs to say several things
 *       without input from the user
 *    OR
 *     - An "options" property that defines the choices a user can take this is an
 *       array of option objects
 * 
 * An options object should have:
 *  - a "text" property that is the label for the user's choice
 *  AND EITHER
 *  - a "next" property that defines the next chat entry by stating a numerical key of
 *    the chat object and is used when the user selects this option
 *  OR
 *  - a "url" property that defines a link for the user to be taken to
 * 
 * A simple example chat object is:
 * const chat = {
 *     1: {
 *         text: 'Good morning sir',
 *         next: 2
 *     },
 *     2: {
 *         text: 'Would you like tea or coffee with your breakfast?',
 *         options: [
 *             {
 *                 text: 'Tea',
 *                 next: 3
 *             },
 *             {
 *                 text: 'Coffee',
 *                 next: 4
 *             }
 *         ]
 *     },
 *     3: {
 *         text: 'Splendid - a fine drink if I do say so myself.'
 *     },
 *     4: {
 *         text: 'As you wish, sir'
 *     }
 * }
 */
const chat = {
    1: {
        text: 'Hi! Welcome to Learnly.',
        options: [
            {
                text: 'Hello! 👋',
                next: 2
            }
        ]
    },
    2: {
        text: 'Hey, we have noticed that you are not paying attention to the lectures',
        next: 3
    },
    3: {
        text: 'Please answer these questions ?',
        options: [
            {
                text: "<strong>Ok</strong>, I Will!",
                next: 4
            },
        ]
    },
    4: {
        text: 'Awesome !',
        next: 5
    },
    5: {
        text: 'What is the key word used to print a statement in java?',
        options: [
            {
                text: "printf()",
                next: 7
            },
            {
                text: "println()",
                next: 6
            }
        ]
    },
    6: {
        text: 'Correct Answer 👍',
        next: 8
    },
    7: {
        text: 'Wrong Answer 👎',
        next: 8
    },
    8: {
        text: 'What is the key word that is used to specify a method not have to return the value?',
        options: [
            {
                text: "Void",
                next: 9
            },
            {
                text: "return",
                next: 10
            },
            {
                text: "module",
                next: 10
            }
        ]
    },
    9: {
        text: 'Correct Answer',
        next: 11
    },
    10: {
        text: 'Wrong Answer 👎',
        next: 11
    },
    11: {
        text: 'What is the keyword used to import a package, class or interface in java?',
        options: [
            {
                text: "package",
                next: 13
            },
            {
                text: "Implements",
                next: 13
            },
            {
                text: "Import",
                next: 12
            }
        ]
    },
    12: {
        text: 'Correct Answer',
        next: 14
    },
    13: {
        text: 'Wrong Answer 👎',
        next: 14
    },
    14: {
        text: 'What is the keyword used stop the execution of a function and to return the desired output',
        options: [
            {
                text: "Native",
                next: 16
            },
            {
                text: "Return",
                next: 15
            },
            {
                text: "Catch",
                next: 16
            }
        ]
    },
    15: {
        text: 'Correct Answer',
        next: 17
    },
    16: {
        text: 'Wrong Answer 👎',
        next: 17
    },
    17: {
        text: 'What is the keyword used Marks a block of code in switch statements?',
        options: [
            {
                text: "Class",
                next: 19
            },
            {
                text: "Try",
                next: 19
            },
            {
                text: "Case",
                next: 18
            }
        ]
    },
    18: {
        text: 'Correct Answer',
        next: 20
    },
    19: {
        text: 'Wrong Answer 👎',
        next: 20
    },
    20: {
        text: 'What is the keyword used to create a Class level variable in java?',
        options: [
            {
                text: "Static",
                next: 21
            },
            {
                text: "Import",
                next: 22
            },
            {
                text: "Module",
                next: 22
            }
        ]
    },
    21: {
        text: 'Correct Answer',
        next: 23
    },
    22: {
        text: 'Wrong Answer 👎',
        next: 23
    },
    23: {
        text: 'What is the keyword used as a access modifier which is used for classes, attributes, methods and constructors, making them accessible by any other class?',
        options: [
            {
                text: "Default",
                next: 25
            },
            {
                text: "Extends",
                next: 25
            },
            {
                text: "Public",
                next: 24
            }
        ]
    },
    24: {
        text: 'Correct Answer',
        next: 26
    },
    25: {
        text: 'Wrong Answer 👎',
        next: 26
    },
    26: {
        text: 'What is the keyword used to terminates the loop immediately, and to move the control of the program to the next statement following the loop',
        options: [
            {
                text: "Break",
                next: 27
            },
            {
                text: "Package",
                next: 28
            },
            {
                text: "Final",
                next: 28
            }
        ]
    },
    27: {
        text: 'Correct Answer',
        next: 29
    },
    28: {
        text: 'Wrong Answer 👎',
        next: 29
    },
    29: {
        text: 'What is the keyword use to export a package with the module',
        options: [
            {
                text: "Try",
                next: 31
            },
            {
                text: "Export",
                next: 30
            },
            {
                text: "Transient",
                next: 31
            }
        ]
    },
    30: {
        text: 'Correct Answer',
        next: 32
    },
    31: {
        text: 'Wrong Answer 👎',
        next: 32
    },
    32: {
        text: 'What is the keyword that is used as a access modifier used for attributes, methods and constructors, making them only accessible within the declared class?',
        options: [
            {
                text: "Return",
                next: 34
            },
            {
                text: "Static",
                next: 34
            },
            {
                text: "Private",
                next: 33
            }
        ]
    },
    33: {
        text: 'Correct Answer 👍',
        next: 35
    },
    34: {
        text: 'Wrong Answer 👎',
        next: 35
    },
    35: {
        text: ' Thank You for contributing with Learnly 🙂',
        next: 36
    },

    36: {
        text: 'Please pay more attention for your lectures 😇',
    },
    // 5: {
    //     text: 'Aah, you\'re missing out!',
    //     next: 7
    // },
    // 6: {
    //     text: 'You have done the quiz',
    //     options: [
    //         {
    //             text: "Good Job !"
    //         }
    //     ]
    // }
};

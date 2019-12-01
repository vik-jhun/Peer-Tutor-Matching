A centralized system that facilitates a peer-tutor platform on college campuses.

A win-win model because:

Students who have taken the same course can be the most effective tutors for current students.
For students who excelled in a course, being a tutor allows them to retain the information and help others.
Functionality: The main page has two buttons: learn and teach. The 'learn' is for tutees, and the 'teach' is for tutors. If the 'teach' button is pressed, it directs the potential tutor to a different page, where they can input their name, major, course (that they are interested in tutoring for), and email. If the 'learn' button is pressed, it directs the potential tutee to a page where they can see a list of tutors available. There is a 'return' button for if the user wants to do a new search. The learn button looks through the dictionary on the server-side by major and by course code. The user can use both or just one.

Ideally, the tutee would reach out to the tutor through email or other social media and arrange a tutoring schedule.

Limitations: This project can benefit from more user-friendly functions like a chat-box, the ability for tutors to remove themselves from the list, and javascript form validation.

Note: If you would like better website design, I will happily share function HTML and CSS files for this web-app upon request.

How it works: 

The landing page mimics the functionality of a POST method through the submit button. A user can submit two choices: teach or learn. 
Use case for teach: The teach functions effectively collects 4 data-points and compiles this in a unified string. When you submit this information, the unified string gets appended to an array of the form NameCourseMajorEmail. This constitutes a dictionary, with frequent user postings, this dictionary gets populated enough to need a key to be indexed. This is where the Learn part of the application comes in. 
Use case for learn: The learn page employes a similar post method, the output here acts as the key for the dictionary populated by the teach part of the application. By entering one key, the rest of the information in the string is given out. 

'''
Xpath: 

//tagName : will select all elements tags
Eg: //h1 : will select all h1 elements

//h1[2]: select 2nd h1 element from html code

//h1[@attribute = "value]: will select h1 elements whose attribute is equal to the value

//h1[contains(@attributeName, "value")]
//h1[(expression1) and (expression2)] #or can also be used

functions
//h1[contains(text(), "Login")]

<input id="email_9876" />
//input[starts-with(@id, "email_")]

//button[text()= "submit"]
 //button[contains(., "Submit")] # . means full Node text

 <button>   Login   </button>
 //button[normalize-space()="Login"]

  //div[last()]
   //div[last()-1]

 //input[not(@type="hidden")]
 select all visible inputs

//input[@type="text" and contains(@id,"user")]
//button[text()="Login" or text()="Sign in"]

(.) : Complete text from current node
text(): direct text only
(..) : select parent node content
(*) ; select child nodes content

use below xpath for below html
<button><span>Login</span></button>
 //button[.="Login"]

'''
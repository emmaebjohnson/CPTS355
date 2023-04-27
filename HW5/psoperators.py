from colors import *
from psexpressions import StringValue, DictionaryValue, CodeArrayValue

#EMMA JOHNSON 
#CPTS 355 HW5
class PSOperators:
    def __init__(self, scoperrule):
        #stack variables
        self.opstack = []  #assuming top of the stack is the end of the list
        self.dictstack = []  #assuming top of the stack is the end of the list
        self.scope = scoperrule
        # The environment that the REPL evaluates expressions in.
        # Uncomment this dictionary in part2
        self.builtin_operators = {
            "add":self.add,
            "sub":self.sub,
            "mul":self.mul,
            "mod":self.mod,
            "eq":self.eq,
            "lt": self.lt,
            "gt": self.gt,
            "dup": self.dup,
            "exch":self.exch,
            "pop":self.pop,
            "copy":self.copy,
            "count": self.count,
            "clear":self.clear,
            "stack":self.stack,
            "dict":self.psDict,
            "string":self.string,
            "length":self.length,
            "get":self.get,
            "put":self.put,
            "getinterval":self.getinterval,
            "putinterval":self.putinterval,
            "search" : self.search,
            "def":self.psDef,
            "if":self.psIf,
            "ifelse":self.psIfelse,
            "for":self.psFor
        }
    #------- Operand Stack Helper Functions --------------
    
    """
        Helper function. Pops the top value from opstack and returns it.
    """
    def opPop(self):
        if len(self.opstack) > 0:
            x = self.opstack[len(self.opstack) - 1]
            self.opstack.pop(len(self.opstack) - 1)
            return x
        else:
            print("Error: opPop - Operand stack is empty")

    """
       Helper function. Pushes the given value to the opstack.
    """
    def opPush(self,value):
        self.opstack.append(value)

    #------- Dict Stack Helper Functions --------------
    """
       Helper function. Pops the top dictionary from dictstack and returns it.
    """  
    def dictPop(self):
        if len(self.dictstack) > 0:
            x = self.dictstack[len(self.dictstack) - 1]
            self.dictstack.pop(len(self.dictstack) - 1)
            return x
        else:
            print("Error: opPop - Dict stack is empty")

    """
       Helper function. Pushes the given dictionary onto the dictstack. 
    """   
    def dictPush(self, link, d):
        if (self.scope == "static"):
            self.dictstack.append((link, d))
        else: 
             self.dictstack.append(d)
        

    """
       Helper function. Adds name:value pair to the top dictionary in the dictstack.
       (Note: If the dictstack is empty, first adds an empty dictionary to the dictstack then adds the name:value to that. 
    """  
    def define(self, name, value):
        if self.scope == "static":
            if len(self.dictstack) <= 0:
                self.dictstack.append((0, {}))

            self.dictstack[len(self.dictstack) - 1][1][name] = value
        else:
            if len(self.dictstack) <= 0:
                self.dictstack.append({})

            self.dictstack[len(self.dictstack) - 1][name] = value
        

    """
       Helper function. Searches the dictstack for a variable or function and returns its value. 
       (Starts searching at the top of the dictstack; if name is not found returns None and prints an error message.
        Make sure to add '/' to the begining of the name.)
    """  
    def lookup(self,name):
        if self.scope == "dynamic":
            dictIndex = len(self.dictstack) - 1
            while (dictIndex >= 0):
                if ('/' + name) in self.dictstack[dictIndex]:
                    return self.dictstack[dictIndex]['/' + name] 
                dictIndex -= 1
            '''
            while((len(self.dictstack) - i) >= 0):
                x = self.dictstack[len(self.dictstack) - i]
                i = i + 1
                if ('/' + name) in x:
                    return x[('/'+ name)]
                elif ('/' + name) in x.values():
                    for key, value in x.items():
                        if ('/'+ name) == value:
                            return key
            '''
        if self.scope == "static":
            def helper(tL, k, ind):
                if k in tL[ind][1]:
                    return tL[ind][1][k]
                else:
                    if ind == 0:
                            return None
                    else:
                            staticIndex = helper(tL, k, tL[ind][0])
                            return staticIndex
            return helper (self.dictstack, '/' + name, len(self.dictstack) -1)
            
        print("error")
        return None
    """Helper function: Static_Link determines the static link to push to the dictionary"""
    def static_link(self, d):
        def helper(tL, k, ind):
            if k in tL[ind][1]:
                return ind
            else:
                if ind == 0:
                        return len(self.dictstack) - 1
                else:
                        return helper(tL, k, tL[ind][0])
        return helper (self.dictstack, ('/' + str(d)), len(self.dictstack) -1)
    #------- Arithmetic Operators --------------

    """
       Pops 2 values from opstack; checks if they are numerical (int); adds them; then pushes the result back to opstack. 
    """  
    def add(self):
        if len(self.opstack) > 1:
            op1 = self.opPop()
            op2 = self.opPop()
            if (isinstance(op1,int) or isinstance(op1,float))  and (isinstance(op2,int) or isinstance(op2,float)):
                self.opPush(op1 + op2)
            else:
                print("Error: add - one of the operands is not a number value")
                self.opPush(op1)
                self.opPush(op2)             
        else:
            print("Error: add expects 2 operands")

    """
       Pops 2 values from opstack; checks if they are numerical (int); subtracts them; and pushes the result back to opstack. 
    """ 
    def sub(self):
        if len(self.opstack) > 1:
            op1 = self.opPop()
            op2 = self.opPop()
            if (isinstance(op1,int) or isinstance(op1,float))  and (isinstance(op2,int) or isinstance(op2,float)):
                self.opPush(op2 - op1)
            else:
                print("Error: sub - one of the operands is not a number value")
                self.opPush(op1)
                self.opPush(op2)             
        else:
            print("Error: add expects 2 operands")

    """
        Pops 2 values from opstack; checks if they are numerical (int); multiplies them; and pushes the result back to opstack. 
    """
    def mul(self):
        if len(self.opstack) > 1:
            op1 = self.opPop()
            op2 = self.opPop()
            if (isinstance(op1,int) or isinstance(op1,float))  and (isinstance(op2,int) or isinstance(op2,float)):
                self.opPush(op1 * op2)
            else:
                print("Error: mul - one of the operands is not a number value")
                self.opPush(op1)
                self.opPush(op2)             
        else:
            print("Error: add expects 2 operands")

    """
        Pops 2 values from stack; checks if they are int values; calculates the remainder of dividing the bottom value by the top one; 
        pushes the result back to opstack.
    """
    def mod(self):
        if len(self.opstack) > 1:
            op1 = self.opPop()
            op2 = self.opPop()
            if (isinstance(op1,int) or isinstance(op1,float))  and (isinstance(op2,int) or isinstance(op2,float)):
                self.opPush(op2 % op1)
            else:
                print("Error: add - one of the operands is not a number value")
                self.opPush(op1)
                self.opPush(op2)             
        else:
            print("Error: add expects 2 operands")

    """ Pops 2 values from stacks; if they are equal pushes True back onto stack, otherwise it pushes False.
          - if they are integers or booleans, compares their values. 
          - if they are StringValue values, compares the `value` attributes of the StringValue objects;
          - if they are DictionaryValue objects, compares the objects themselves (i.e., ids of the objects).
        """
    def eq(self):
        if len(self.opstack) > 1:
            op1 = self.opPop()
            op2 = self.opPop()
            if (isinstance(op1,int) or isinstance(op1,bool))  and (isinstance(op2,int) or isinstance(op2, bool)):
                if (op1 == op2):
                  self.opPush(True)
                elif (op1 != op2):
                    self.opPush(False)
            elif (isinstance(op1,StringValue)) and (isinstance(op2,StringValue)):
                if ((op1.value == op2.value)):
                  self.opPush(True)
                else:
                    self.opPush(False)
            elif (isinstance(op1,DictionaryValue)) and (isinstance(op2,DictionaryValue)):
                if (op1 == op2):
                  self.opPush(True)
                else:
                    self.opPush(False)            
        else:
            print("Error: add expects 2 operands")

    """ Pops 2 values from stacks; if the bottom value is less than the second, pushes True back onto stack, otherwise it pushes False.
          - if they are integers or booleans, compares their values. 
          - if they are StringValue values, compares the `value` attributes of them;
          - if they are DictionaryValue objects, compares the objects themselves (i.e., ids of the objects).
    """  
    def lt(self):
        if len(self.opstack) > 1:
            op1 = self.opPop()
            op2 = self.opPop()
            if (isinstance(op1,int) or isinstance(op1,bool))  and (isinstance(op2,int) or isinstance(op2, bool)):
                if (op1 > op2):
                  self.opPush(True)
                else:
                    self.opPush(False)
            elif (isinstance(op1,StringValue)) and (isinstance(op2,StringValue)):
                if ((op1.value > op2.value)):
                  self.opPush(True)
                else:
                    self.opPush(False)
            elif (isinstance(op1,DictionaryValue)) and (isinstance(op2,DictionaryValue)):
                if (op1 > op2):
                  self.opPush(True)
                else:
                    self.opPush(False)  
                      
        else:
            print("Error: add expects 2 operands")
      


    """ Pops 2 values from stacks; if the bottom value is greater than the second, pushes True back onto stack, otherwise it pushes False.
          - if they are integers or booleans, compares their values. 
          - if they are StringValue values, compares the `value` attributes of them;
          - if they are DictionaryValue objects, compares the objects themselves (i.e., ids of the objects).
    """  
    def gt(self):
        if len(self.opstack) > 1:
            op1 = self.opPop()
            op2 = self.opPop()
            if (isinstance(op1,int) or isinstance(op1,bool))  and (isinstance(op2,int) or isinstance(op2, bool)):
                if (op1 < op2):
                  self.opPush(True)
                elif (op1 != op2):
                    self.opPush(False)
            elif (isinstance(op1,StringValue)) and (isinstance(op2,StringValue)):
                if ((op1.value < op2.value)):
                  self.opPush(True)
                else:
                    self.opPush(False)
            elif (isinstance(op1,DictionaryValue)) and (isinstance(op2,DictionaryValue)):
                if (op1 < op2):
                  self.opPush(True)
                else:
                    self.opPush(False)  
                 
        else:
            print("Error: add expects 2 operands")
   

    #------- Stack Manipulation and Print Operators --------------
    """
       This function implements the Postscript "pop operator". Calls self.opPop() to pop the top value from the opstack and discards the value. 
    """
    def pop (self):
        if (len(self.opstack) > 0):
            self.opPop()
        else:
            print("Error: pop - not enough arguments")

    """
       Prints the opstack and dictstack. The end of the list is the top of the stack. 
    """
    def stack(self):
       
        print(OKGREEN+"===**opstack**===")
        for item in reversed(self.opstack):
            print(item)
        print("-----------------------"+CEND)
        print(RED+"===**dictstack**===")
        m = len(self.dictstack) - 1
        for item in reversed(self.dictstack):
            if self.scope == "static":
                print("---" + str(m) + "---" + str(item[0]) + "---")
                for key in item[1]:
                    print( str(key) + " " + str(item[1][key]))

                m = m -1
            else: 
                m = len(self.dictstack) - 1
                for key in item:
                    print("---" + str(m) + "---" + '0' + "---")
                    print( str(key) + " " + str(item[key]))
                    m = m -1
        print("-----------------------"+ CEND)


    """
       Copies the top element in opstack.
    """
    def dup(self):
        if (len(self.opstack) > 0):
         self.opPush(self.opstack[len(self.opstack) - 1])
        
    """
       Pops an integer count from opstack, copies count number of values in the opstack. 
    """
    def copy(self):
        if (len(self.opstack) > 0):
         num = self.opPop()

        index = len(self.opstack)
        while((num != 0) and (self.opstack != None)):
            self.opPush(self.opstack[index - num])
            num -= 1

    """
        Counts the number of elements in the opstack and pushes the count onto the top of the opstack.
    """
    def count(self):
       self.opPush(len(self.opstack))

    """
       Clears the opstack.
    """
    def clear(self):
        while (len(self.opstack) > 0):
            self.opPop()
        
    """
       swaps the top two elements in opstack
    """
    def exch(self):
        if (len(self.opstack) > 1):
            top = self.opPop()
            second = self.opPop()
            self.opPush(top)
            self.opPush(second)
        else: 
            print("Error: two values are needed in the opstack to swap")

    # ------- String and Dictionary creator operators --------------

    """ Creates a new empty string  pushes it on the opstack.
    Initializes the characters in the new string to \0 , i.e., ascii NUL """
    """ pops an integer value (e.g., n) from the operand stack and
    creates a StringValue object with 'value' of length 'n'. Initializes each character in the
    StringValue‘s 'value'with '\0' , i.e., ascii NUL character."""
   
    def string(self):
        if (len(self.opstack) > 0): # needs integer value <size>
            size = self.opPop()

            if (isinstance(size, int) and size > 0):
                 self.opPush(StringValue('(' + ('\0' * size) + ')'))
            
            else:
                print("Error: string - need a size")
        
        else:
            print("Error: string expects at least one item on opstack")

    """Creates a new empty dictionary  pushes it on the opstack """
    def psDict(self):
        if (len(self.opstack) > 0):
            self.opPop()
            self.opPush(DictionaryValue({}))
    


    # ------- String and Dictionary Operators --------------
    """ Pops a string or dictionary value from the operand stack and calculates the length of it. Pushes the length back onto the stack.
       The `length` method should support both DictionaryValue and StringValue values.
    """
    
    def length(self):
        if (len(self.opstack) > 0):
            value = self.opPop()
            if isinstance(value, StringValue):
                self.opPush(value.length() - 2)

            elif isinstance(value, DictionaryValue):
                self.opPush(value.length())
            else: 
                print("Error: expected string or dictionary value")
        else:
            print("Error: expected an argument")

    """ Pops either:
         -  "A (zero-based) index and an StringValue value" from opstack OR 
         -  "A `name` (i.e., a key) and DictionaryValue value" from opstack.  
        If the argument is a StringValue, pushes the ascii value of the the character in the string at the index onto the opstack;
        If the argument is an DictionaryValue, gets the value for the given `name` from DictionaryValue's dictionary value and pushes it onto the opstack
    """
    def get(self):
        if (len(self.opstack) > 0):
            index = self.opPop()
            value = self.opPop()
            if isinstance(value, StringValue):
                self.opPush(ord(value.value[index + 1])) #ord() -> gets ascii && +1 because '('

            elif isinstance(value, DictionaryValue):
                self.opPush(value.value[index])
            else: 
                print("Error: expected string or dictionary value")
        else:
            print("Error: expected an argument")
   
    """
    Pops either:
    - "An `item`, a (zero-based) `index`, and an StringValue value from  opstack", OR
    - "An `item`, a `name`, and a DictionaryValue value from  opstack". 
    If the argument is a StringValue, replaces the character at `index` of the StringValue's string with the character having the ASCII value of `item`.
    If the argument is an DictionaryValue, adds (or updates) "name:item" in DictionaryValue's dictionary `value`.
    """
    def put(self):
        if (len(self.opstack) > 2):
            item = self.opPop()
            index = self.opPop()
            value = self.opPop()
            if isinstance(value, StringValue):
                value.value = value.value[:(index + 1)] + chr(item) + value.value[(index + 1) + 1:]

            elif isinstance(value, DictionaryValue):
               value.value[index] = item
            
            else: 
                print("Error: expected string or dictionary value")
        else:
            print("Error: expected an argument")
   
    """
    getinterval is a string only operator, i.e., works only with StringValue values. 
    Pops a `count`, a (zero-based) `index`, and an StringValue value from  opstack, and 
    extracts a substring of length count from the `value` of StringValue starting from `index`,
    pushes the substring back to opstack as a StringValue value. 
    """ 
    def getinterval(self):
       if (len(self.opstack) > 2):
            count = self.opPop()
            index = self.opPop()
            value = self.opPop()
            if isinstance(value, StringValue):
                newstring = "("
                while (count != 0 and value.value[index+1] is not None):
                    newstring += value.value[index+1]
                    count -= 1
                    index += 1
                self.opPush(StringValue(newstring + ')'))
               # self.opPush(value) #ord() -> gets ascii && +1 because '('

    """
    putinterval is a string only operator, i.e., works only with StringValue values. 
    Pops a StringValue value, a (zero-based) `index`, a `substring` from  opstack, and 
    replaces the slice in StringValue's `value` from `index` to `index`+len(substring)  with the given `substring`s value. 
    """
    def putinterval(self):
       if (len(self.opstack) > 2):
            substring = self.opPop()
            index = self.opPop()
            value = self.opPop()
            
            if isinstance(substring, StringValue) and isinstance(index, int) and isinstance(value, StringValue):
                value.value = value.value[:index + 1] + substring.value[1:-1] + value.value[index + len(substring.value) - 1:]
       else: print("Error:expected 3 arguments")

    """
    search is a string only operator, i.e., works only with StringValue values. 
    Pops two StringValue values: delimiter and inputstr
    if delimiter is a sub-string of inputstr then, 
       - splits inputstr at the first occurence of delimeter and pushes the splitted strings to opstack as StringValue values;
       - pushes True 
    else,
        - pushes  the original inputstr back to opstack
        - pushes False
    """
    def search(self):
        if (len(self.opstack) > 1):
            delim = self.opPop()
            inputstr = self.opPop()
            
            if isinstance(delim, StringValue) and isinstance(inputstr, StringValue):
                if delim.value[1] in inputstr.value: 
                    i = inputstr.value.find(delim.value[1])
                    self.opPush(StringValue('(' + inputstr.value[i+1:] ))
                    self.opPush(StringValue( delim.value ))
                    self.opPush(StringValue(inputstr.value[:i] + ')'))
                    self.opPush(True)
                else: 
                    self.opPush(inputstr)
                    self.opPush(False)
            else: 
                print("Error: expected type(s) of StringValue")
        else: 
            print("Error: expected two arguments")

    # ------- Operators that manipulate the dictstact --------------
        
    """ Pops a name and a value from stack, adds the definition to the dictionary at the top of the dictstack. """
    def psDef(self):
       # if (len(self.opstack) > 1):
            value = self.opPop()
            name = self.opPop()
            self.define(name, value)
        # else:
        #     print("Error: expected 2 arguments")

    # ------- if/ifelse Operators --------------
    """ if operator
        Pops a CodeArrayValue object and a boolean value, if the value is True, executes (applies) the code array by calling apply.
       Will be completed in part-2. 
    """
    def psIf(self):
        codearray = self.opPop()
        boolvalue = self.opPop()
        # if isinstance(boolvalue, CodeArrayValue):
        #    boolvalue = boolvalue.apply(self)
        if isinstance (codearray, CodeArrayValue) and isinstance(boolvalue, bool):
            if(boolvalue is True):
                static_link = self.dictstack[len(self.dictstack) - 1][0]
                codearray.apply(self, static_link)
        else: print("Error: expected a codearray and a bool")

    """ ifelse operator
        Pops two CodeArrayValue objects and a boolean value, if the value is True, executes (applies) the bottom CodeArrayValue otherwise executes the top CodeArrayValue.
        Will be completed in part-2. 
    """
    def psIfelse(self):
        codearray_top = self.opPop()
        codearray_bottom = self.opPop()
        boolvalue = self.opPop()
        if isinstance (codearray_top, CodeArrayValue) and isinstance (codearray_bottom, CodeArrayValue) and isinstance(boolvalue, bool):
            static_link = self.dictstack[len(self.dictstack) - 1][0]
            if(boolvalue is True):
                codearray_bottom.apply(self, static_link)
            else:
                codearray_top.apply(self, static_link)
        else: print("Error: expected 2 codearrays and a bool")


    #------- Loop Operators --------------
    """
       Implements for operator.   
       Pops a CodeArrayValue object, the end index (end), the increment (inc), and the begin index (begin) and 
       executes the code array for all loop index values ranging from `begin` to `end`. 
       Pushes the current loop index value to opstack before each execution of the CodeArrayValue. 
       Will be completed in part-2. 
    """ 
    def psFor(self):
        codearray = self.opPop()
        end = self.opPop()
        inc = self.opPop()
        begin = self.opPop()

        if isinstance (codearray, CodeArrayValue) and isinstance (end, int) and isinstance(inc, int) and isinstance(begin, int):
            for i in range (begin, end + inc, inc): 
                self.opPush(i)
                static_link = self.dictstack[len(self.dictstack) - 1][0]
                codearray.apply(self, static_link)
        else: print("Error: arguments on OpStack of incorrect type")

    """ Cleans both stacks. """      
    def clearBoth(self):
        self.opstack[:] = []
        self.dictstack[:] = []

    """ Will be needed for part2"""
    def cleanTop(self):
        if len(self.opstack)>1:
            if self.opstack[-1] is None:
                self.opstack.pop()
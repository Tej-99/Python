'''
operators have different levels of precedence, which determine the order in which they are evaluated.
when multiple operators are present in an expression, the ones with higher precedence are evaluated first.
In case of same precedence , their associativity comes int play, determinig the order of evaluation.
'''
# order        operator                        associativity
'''
 1               ()                            left to right
 
 2        x[index],x[index:index]              left to right
 
 3             await x                              N/A
 
 4                **                           right to left
 
 5          +x, -x, ~x                         right to left
 
 6          *, @, /, //, %                     left to right
 
 7               +, -                          left to right
 
 8            <<, >>                           left to right
 
 9              &                              left to right
 
 10             ^                              left to right
 
 11             |                              left to right
 
 12       in, not in, is,  is not,             left to right
            <, <=, >, >=, !=, ==
            
 13             not x                          right to left
 
 14             and                            left to right
 
 15             or                             left to right
 
 16            if-else                         right to left
 
 17            lambda                               N/A
 
 18             :=                             right to left           

'''
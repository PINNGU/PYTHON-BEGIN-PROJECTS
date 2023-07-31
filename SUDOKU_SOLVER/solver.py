

class Solver():

     table = [
               [0,3,7,8,0,1,0,0,0],
               [0,0,0,0,0,0,0,4,3],
               [5,0,0,0,0,0,0,0,0],
               [0,0,0,0,7,0,8,0,0],
               [0,0,0,0,0,0,1,0,0],
               [0,2,0,0,3,0,0,0,0],
               [6,0,2,0,0,0,0,7,5],
               [0,0,3,4,0,0,0,0,0],
               [0,0,0,2,0,0,6,8,4]
            ]
    


     def possible(self,num,row,col):

          for i in range(0,9):
               if num == self.table[row][i]:
                    return False
            
          for i in range(0,9):
               if num == self.table[i][col]:
                    return False
          
          box_row = row // 3 * 3
          box_col = col // 3 * 3
     
          for i in range(box_row,box_row + 3):
               for k in range(box_col,box_col + 3):
                    if num == self.table[i][k]:
                         return False
                      
          return True
    
     def game_solve(self):
          for n in range(9):
               for m in range(9):
                    if self.table[n][m] == 0:
                         for num in range(1,10):
                              if self.possible(num,n,m):
                                 self.table[n][m] = num
                                 self.game_solve()
                                 self.table[n][m] = 0
                         
                         return
                    
          self.file_write()

     def file_write(self):
          f = open("solution.txt","w")
          for i in range(0,9):
               f.write(str(self.table[i]))
               f.write("\n")
          
          f.close()
          quit()

    

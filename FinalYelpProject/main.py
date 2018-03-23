#Gautam Mehta, Chris Gentibano, Aiden Sun
from tkinter import *
import tkinter as tk
import tkinter.messagebox as tkmb
import tkinter.filedialog
import sqlite3
import matplotlib
import webbrowser
matplotlib.use("TkAgg")
from matplotlib import pyplot as plt

from PIL import Image, ImageTk

class FindWin(tk.Tk):
    def __init__(self):
        super().__init__()
        conn = sqlite3.connect('yelp.db')
        self.cur = conn.cursor() 
        self.config(bg ='white')
        self.title('Fast Foods Near Deanza')
        self.resizable(False, True)
        
        priceLabel = tk.Label(self, text='Price')
        priceLabel.grid(row=0, column=0, sticky='w')
        priceLabel.config(bg ='white')
        
        ratingLabel = tk.Label(self, text='Rating')
        ratingLabel.grid(row=0, column=1, sticky='w')
        ratingLabel.config(bg ='white')
        
        reviewCountLabel = tk.Label(self, text='Review Count')
        reviewCountLabel.grid(row=0, column=2, sticky='w')
        reviewCountLabel.config(bg ='white')
        
        self.filterRe = tk.StringVar()
        priceRB1 = tk.Radiobutton(self, text="$", variable=self.filterRe, value='$', command=self.__applyPriceFilter)
        priceRB1.grid(row=1, column=0, sticky='w')
        priceRB1.config(bg ='white')
        
        priceRB2 = tk.Radiobutton(self, text="$$", variable=self.filterRe, value='$$', command=self.__applyPriceFilter)
        priceRB2.grid(row=2, column=0, sticky='w')
        priceRB2.config(bg ='white')
        
        priceRB3 = tk.Radiobutton(self, text="$$$", variable=self.filterRe, value='$$$', command=self.__applyPriceFilter)
        priceRB3.grid(row=3, column=0, sticky='w')  
        priceRB3.config(bg ='white')
        
        ratingRB1 = tk.Radiobutton(self, text="1-2 stars", variable=self.filterRe, value='1-2', command=self.__applyRatingFilter)
        ratingRB1.grid(row=1, column=1, sticky='w')
        ratingRB1.config(bg ='white')
        
        ratingRB2 = tk.Radiobutton(self, text="2-3 stars", variable=self.filterRe, value='2-3', command=self.__applyRatingFilter)
        ratingRB2.grid(row=2, column=1, sticky='w')
        ratingRB2.config(bg ='white')
        
        ratingRB3 = tk.Radiobutton(self, text="3-4 stars", variable=self.filterRe, value='3-4', command=self.__applyRatingFilter)
        ratingRB3.grid(row=3, column=1, sticky='w') 
        ratingRB3.config(bg ='white')
        
        ratingRB4 = tk.Radiobutton(self, text="4-5 stars", variable=self.filterRe, value='4-5', command=self.__applyRatingFilter)
        ratingRB4.grid(row=4, column=1, sticky='w')        
        ratingRB4.config(bg ='white')

        reviewCountRB1 = tk.Radiobutton(self, text="0-300", variable=self.filterRe, value='0-300', command=self.__applyRevCountFilter)
        reviewCountRB1.grid(row=1, column=2, sticky='w')
        reviewCountRB1.config(bg ='white')
        
        reviewCountRB2 = tk.Radiobutton(self, text="300-600", variable=self.filterRe, value='300-600', command=self.__applyRevCountFilter)
        reviewCountRB2.grid(row=2, column=2, sticky='w')
        reviewCountRB2.config(bg ='white')
        
        reviewCountRB3 = tk.Radiobutton(self, text="600-900", variable=self.filterRe, value='600-900', command=self.__applyRevCountFilter)
        reviewCountRB3.grid(row=3, column=2, sticky='w')   
        reviewCountRB3.config(bg ='white')
        
        reviewCountRB4 = tk.Radiobutton(self, text="900-1300", variable=self.filterRe, value='900-1300', command=self.__applyRevCountFilter)
        reviewCountRB4.grid(row=4, column=2, sticky='w')       
        reviewCountRB4.config(bg ='white')
        
        self.filterRe.set('$')
        
        img = PhotoImage(file='yelplogo.gif')
        logo = tk.Label(self, image=img)
        logo.grid(row=0, column=3, rowspan=4)
        logo.image = img
        logo.config(bg = 'white')
        logo.bind("<Button-1>", self.__openWeb)
        
        scrollbar = tk.Scrollbar(self)
        self.resultListBox = tk.Listbox(self, yscrollcommand=scrollbar.set)
        self.resultListBox.grid(row=5, columnspan=4, rowspan=2, sticky='nesw')
        scrollbar.config(command=self.resultListBox.yview)
        scrollbar.grid(row=5, column=5, rowspan=2, sticky='nes')
        self.resultListBox.bind("<Double-Button-1>", self.__onDouble)
        
        total_records=[]
        self.cur.execute("SELECT yid, name, rating, price, total_reviews FROM MainDB")
        for i in self.cur.fetchall():
            total_records.append(str(i[0])+") "+ i[1])
        for item in total_records:
            self.resultListBox.insert(tk.END, item) 
        
        num_Resaurants = tk.Label(self, text='Number of Restaurants:')
        num_Resaurants.grid(row=7, column=0, columnspan=2, sticky='w')
        num_Resaurants.config(bg = 'white')
        
        self.numResults = tk.IntVar()
        labelCount = tk.Label(self, textvariable=self.numResults)
        labelCount.grid(row=7, column=2, sticky='sw')
        labelCount.config(bg = 'white')
        self.numResults.set(self.resultListBox.size())

        clearButton = tk.Button(self, text='Clear Filter', command= self.__clear).grid(row=5, column=6, sticky='es')
        
        analyzeButton = tk.Button(self, text='Analyze', command= self.__finalAnalysis)
        analyzeButton.grid(row=6, column=6, sticky='e')
        analyzeButton.focus_set()
        analyzeButton.bind('<Return>', self.__finalAnalysis)
        
        self.grid_rowconfigure(5, weight=1)        
        
        self.protocol('WM_DELETE_WINDOW', self.__exit)
        self.update()       
    
    def __applyPriceFilter(self):
        choice = self.filterRe.get()
        ratinglist = []
        revlist = []
        namelist = []
        record = []
    
        self.resultListBox.delete(0, tk.END)  
        self.cur.execute("SELECT yid, name, rating, price, total_reviews FROM MainDB WHERE price = ? ORDER BY price", (choice,)) #
        for i in self.cur.fetchall():
            ratinglist.append(i[2])  
            revlist.append(i[4])
            namelist.append(i[1])
            record.append(str(i[0])+") "+ i[1])
        for item in record:
            self.resultListBox.insert(tk.END, item)             
            
        
        self.numResults.set(self.resultListBox.size())
        if int(self.numResults.get()) > 25:
            plt.clf()
            plt.ylabel("Review Count")
            plt.xlabel("Ratings")
        
            ymax = revlist.index(max(revlist))
            ymin = revlist.index(min(revlist))
        
            plt.scatter(ratinglist, revlist, s = 100)
            plt.scatter(ratinglist[ymax],max(revlist), s=100, c='Green', label='Best - ' + namelist[ymax])
            plt.scatter(ratinglist[ymin],min(revlist), s=100, c='Red', label='Worst - ' + namelist[ymin])
            plt.legend(loc="upper left") 
            plt.xlim(0,max(ratinglist)+1)
            plt.ylim(0,max(revlist)+25)
            
            txt = '''
                This is a rating vs review count scatter plot. After the user
                selects their preferred price range, they can also determine 
                the best restaurant by looking for the restaurant with the most
                amount of reviews.'''
            plt.gca().set_position((.1, .25, .8, .6))
            plt.figtext(.02, .02, txt)
            
            plt.show()
        else:
            tkmb.showerror(title="Insufficient data", message="Not enough data to plot. Please click Clear Filter or choose another filter")    
    
    def __applyRatingFilter(self):
        choice = self.filterRe.get()
        choice = choice.split('-')
        LHS = choice[0]
        RHS = choice[1]
        record = []
        pricelist = []
        revlist = []
        namelist = []
        
        self.resultListBox.delete(0, tk.END)  
        self.cur.execute("SELECT yid, name, rating, price, total_reviews FROM MainDB WHERE rating BETWEEN ? AND ? ORDER BY yid", (LHS, RHS))
        for i in self.cur.fetchall():
            pricelist.append(i[3])
            revlist.append(i[4])
            namelist.append(i[1])
            record.append(str(i[0])+") "+ i[1])
        for item in record:
            self.resultListBox.insert(tk.END, item)             
        
        
        self.numResults.set(self.resultListBox.size())
        if int(self.numResults.get()) > 10:
            plt.clf()
            for i in pricelist:
                if i == "$":
                    pricelist[pricelist.index(i)] = 1
                elif i == "$$":
                    pricelist[pricelist.index(i)] = 2   
                elif i == "$$$":
                    pricelist[pricelist.index(i)] = 3               
            plt.ylabel("Price")
            plt.xlabel("Review Count")
        
            ymax = revlist.index(max(revlist))
            ymin = revlist.index(min(revlist))
        
            plt.scatter(revlist,pricelist, s = 100)
            plt.scatter(max(revlist),pricelist[ymax], s=100, c='Green', label='Best - ' + namelist[ymax])
            plt.scatter(min(revlist),pricelist[ymin], s=100, c='Red', label='Worst - ' + namelist[ymin])
            plt.legend(loc="best") 
            plt.xlim(0,max(revlist)+15)
            plt.ylim(0,max(pricelist)+1)
            
            txt = '''
                This is a review count vs price scatter plot. After the user
                selects their preferred rating range, they can also determine 
                the best restaurant by looking for the restaurant with the most
                amount of reviews.'''
            plt.gca().set_position((.1, .25, .8, .6))
            plt.figtext(.02, .02, txt)  
            
            plt.show()
        else:
            tkmb.showerror(title="Insufficient data", message="Not enough data to plot. Please click Clear Filter or choose another filter")
            
    def __applyRevCountFilter(self):
        choice = self.filterRe.get()
        choice = choice.split('-')
        LHS = choice[0]
        RHS = choice[1]
        record = []
        ratinglist = []
        pricelist = []
        namelist = []
        
        self.resultListBox.delete(0, tk.END)  
        self.cur.execute("SELECT yid, name, rating, price, total_reviews FROM MainDB WHERE total_reviews BETWEEN ? AND ? ORDER BY yid", (LHS, RHS))
        for i in self.cur.fetchall():
            pricelist.append(i[3])
            ratinglist.append(i[2])
            namelist.append(i[1])
            record.append(str(i[0])+") "+ i[1])
        for item in record:
            self.resultListBox.insert(tk.END, item)                
        
        self.numResults.set(self.resultListBox.size())
        if int(self.numResults.get()) > 10:
            plt.clf()
            for i in pricelist:
                if i == "$":
                    pricelist[pricelist.index(i)] = 1
                elif i == "$$":
                    pricelist[pricelist.index(i)] = 2   
                elif i == "$$$":
                    pricelist[pricelist.index(i)] = 3  
                    
            plt.ylabel("Price")
            plt.xlabel("Ratings")
        
            ymax = ratinglist.index(max(ratinglist))
            ymin = ratinglist.index(min(ratinglist))
        
            plt.scatter(ratinglist,pricelist,  s = 100, alpha= 0.1)
            plt.scatter(max(ratinglist),pricelist[ymax], s=100, c='Green', label='Best - ' + namelist[ymax])
            plt.scatter(min(ratinglist),pricelist[ymin], s=100, c='Red', label='Worst - ' + namelist[ymin])
            plt.legend(loc="best") 
            plt.xlim(0,max(ratinglist)+1)
            plt.ylim(0.5,max(pricelist)+1)  
            
            txt = '''
                This is a ratings vs price scatter plot. After the user
                selects their preferred review count range, they can also determine 
                the best restaurant by looking for the restaurant with the best rating.'''
            plt.gca().set_position((.1, .25, .8, .6))
            plt.figtext(.02, .02, txt) 
            
            plt.show()
        else:
            tkmb.showerror(title="Insufficient data", message="Not enough data to plot. Please click Clear Filter or choose another filter")
            
    def __onDouble(self, event):
        widget = event.widget
        selection = widget.curselection()
        selection = str(selection[0]) 
        value = widget.get(selection)
        try:
            key = value[0]
            name = value[3:]
            self.cur.execute("SELECT name, rating, price, total_reviews, phone_number, address, LocationDB.cityState FROM MainDB JOIN LocationDB ON MainDB.location = LocationDB.key WHERE yid = ? AND name = ?", (key, name))
            info = self.cur.fetchall()
            name = str(info[0][0])
            rating = str(info[0][1])
            price = str(info[0][2])
            reviews = str(info[0][3])
            digits = str(info[0][4])
            address = str(info[0][5])
            state = str(info[0][6])
            display = 'Name of Restaurant: ' + name + '\nRating: ' + rating + '\nPrice: ' + price + '\nReview Count: ' + reviews + '\nPhone Number: ' + digits + '\nAddress: ' + address + ', ' + state
            tkmb.showinfo(title='Information', message=display)
        except IndexError:
            key = value[0:2]
            name = value[4:]
            self.cur.execute("SELECT name, rating, price, total_reviews, phone_number, address, LocationDB.cityState FROM MainDB JOIN LocationDB ON MainDB.location = LocationDB.key WHERE yid = ? AND name = ?", (key, name))
            info = self.cur.fetchall()
            name = str(info[0][0])
            rating = str(info[0][1])
            price = str(info[0][2])
            reviews = str(info[0][3])
            digits = str(info[0][4])
            address = str(info[0][5])
            state = str(info[0][6])
            info = 'Name of Restaurant: ' + name + '\nRating: ' + rating + '\nPrice: ' + price + '\nReview Count: ' + reviews + '\nPhone Number: ' + digits + '\nAddress: ' + address + ', ' + state
            tkmb.showinfo(title='Information', message=info)  
     
    def __openWeb(self, event):
        webbrowser.open('http://yelp.com')
    
    def __clear(self):
        self.resultListBox.delete(0, tk.END)  
        record = []
        self.cur.execute("SELECT yid, name FROM MainDB")
        for i in self.cur.fetchall():
            record.append(str(i[0])+") "+ i[1])
        for item in record:
            self.resultListBox.insert(tk.END, item)
        
        self.numResults.set(self.resultListBox.size())
        self.filterRe.set('$')
    
    def __finalAnalysis(self, *args):
        plt.clf()
        below3 = []
        above3 = []
        percents = []
        for record in self.cur.execute("SELECT rating FROM MainDB WHERE rating <= 3.0") :
            below3.append(record[0]) 
        for record in self.cur.execute("SELECT rating FROM MainDB WHERE rating > 3.0") :
            above3.append(record[0]) 	
    
        percents.append((len(below3)/50)*100)
        percents.append((len(above3)/50)*100)
        explode = (0, 0.1)
        labels = 'Ratings below 3', 'Ratings above 3'
        plt.pie(percents,explode = explode, labels = labels,autopct='%1.1f%%',shadow=True, startangle=90)
        plt.axis('equal') 
        plt.suptitle('Overall ratings for fast food near De Anza', fontsize=14, fontweight='bold')
        plt.show()
        
    def __exit(self):
        self.destroy()       
        
def main() :
    win = FindWin()
    win.mainloop() 
    
if __name__ == '__main__':
    main()
from wrangler import dw
import sys

if(len(sys.argv) < 3):
	sys.exit('Error: Please include an input and output file.  Example python script.py input.csv output.csv')

w = dw.DataWrangler()

# Split data repeatedly on newline  into  rows
w.add(dw.Split(column=["data"],
               table=0,
               status="active",
               drop=True,
               result="row",
               update=False,
               insert_position="right",
               row=None,
               on="\n",
               before=None,
               after=None,
               ignore_between=None,
               which=1,
               max=0,
               positions=None,
               quote_character=None))

# Split data repeatedly on 'tab'
w.add(dw.Split(column=["data"],
               table=0,
               status="active",
               drop=True,
               result="column",
               update=False,
               insert_position="right",
               row=None,
               on="\t",
               before=None,
               after=None,
               ignore_between=None,
               which=1,
               max=0,
               positions=None,
               quote_character=None))

# Promote row 1  to header
w.add(dw.SetName(column=[],
                 table=0,
                 status="active",
                 drop=True,
                 names=[],
                 header_row=0))

# Delete  rows where Location is null
w.add(dw.Filter(column=[],
                table=0,
                status="active",
                drop=False,
                row=dw.Row(column=[],
             table=0,
             status="active",
             drop=False,
             conditions=[dw.IsNull(column=[],
                table=0,
                status="active",
                drop=False,
                lcol="Location",
                value=None,
                op_str="is null")])))

# Fold 2003, 2004, 2005, 2006...  using  header as a key
w.add(dw.Fold(column=["_2003","_2004","_2005","_2006","_2007","_2008","_2009","_2010","_2011","_2012","_2013","_2014","_2015","_2016","_2017","_2018","_2019"],
              table=0,
              status="active",
              drop=False,
              keys=[-1]))

# Set  fold  name to  year
w.add(dw.SetName(column=["fold"],
                 table=0,
                 status="active",
                 drop=True,
                 names=["year"],
                 header_row=None))

# Delete  rows where value is null
w.add(dw.Filter(column=[],
                table=0,
                status="active",
                drop=False,
                row=dw.Row(column=[],
             table=0,
             status="active",
             drop=False,
             conditions=[dw.IsNull(column=[],
                table=0,
                status="active",
                drop=False,
                lcol="value",
                value=None,
                op_str="is null")])))

w.apply_to_file(sys.argv[1]).print_csv(sys.argv[2])

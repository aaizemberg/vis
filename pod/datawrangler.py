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

# Cut from pos on 'a'
w.add(dw.Cut(column=["pos"],
             table=0,
             status="active",
             drop=False,
             result="column",
             update=True,
             insert_position="right",
             row=None,
             on="a",
             before=None,
             after=None,
             ignore_between=None,
             which=1,
             max=1,
             positions=None))

# Delete  rows where pos is null
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
                lcol="pos",
                value=None,
                op_str="is null")])))

# Fill categoria  with values from above
w.add(dw.Fill(column=["categoria"],
              table=0,
              status="active",
              drop=False,
              direction="down",
              method="copy",
              row=None))

# Fill n_categoria  with values from above
w.add(dw.Fill(column=["n_categoria"],
              table=0,
              status="active",
              drop=False,
              direction="down",
              method="copy",
              row=None))

w.apply_to_file(sys.argv[1]).print_csv(sys.argv[2])

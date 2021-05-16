#pip install csv
#pip install fpdf
#pip install jsons
def CSVtoPDF(Location,Title,Title_font='Times',Title_style='B',Title_size=14,Title_border=0,Title_link=' ',
           Header=1,Header_start=0,Header_end=17,Body_align='C',end_of_report_text=' ',File_dest='F',cols=[]):
       
    import csv
    from fpdf import FPDF

    if cols!=[]:
        import pandas as pd
        df=pd.read_csv(Location)
        df=df[df.columns[cols]]
        df.to_csv('temp.csv',index=False)
        Location='temp.csv'
        
    with open(Location, newline='') as f:
        reader = csv.reader(f)
        for row in reader:
            pdf = FPDF()
            pdf.add_page()
            page_width = pdf.w - 2 * pdf.l_margin
            pdf.set_font(Title_font,Title_style,Title_size)
            if Title_link==' ':

                pdf.cell(page_width,h=8, txt=Title, align='C',border=Title_border,link=Title_link)
            else:
                pdf.cell(page_width,h=8, txt=Title, align='C',border=Title_border)

            pdf.ln(10)
            pdf.set_font('Times', '', 11)
            col_width = page_width/len(row)
            pdf.ln(1)
            fz = pdf.font_size
            if Header==1:
                for j in range (len(row)):
                    pdf.cell(col_width,fz,row[j][Header_start:Header_end],border=1,align='C')
                pdf.ln(fz)

            for row in reader:
                for i in range(len(row)):
                    check= '.' in row[i]
                    if (check):
                        pdf.cell(col_width,fz,row[i].split('.')[0]+'.'+(row[i].split('.')[1][:2]),border=1,align=Body_align)
                    else:
                        pdf.cell(col_width,fz,row[i],border=1,align=Body_align)
                pdf.ln(fz)

            pdf.ln(10)
            if end_of_report_text!=' ':
                pdf.set_font('Times','',10.0) 
                pdf.cell(page_width, 0.0,txt=end_of_report_text, align='C')

            pdf.output(name=Title+'.pdf', dest=File_dest)
    if cols!=[]:
        import os
        os.remove('temp.csv')

           
           
           
           
#############################################################################################

#########################################################################################################################

def jsontocsv(Input_File,Output_File,Dataset_Name='NULL',header=1):
    import json
    import csv
    with open(Input_File) as json_file:
        data=json.load(json_file)
    if Dataset_Name!='NULL':
        data=data[Dataset_Name]
    O_file=open(Output_File+'.csv','w')
    csv_writer=csv.writer(O_file)
    for d in data:
        if header==1:
            h=d.keys()
            csv_writer.writerow(h)
            header+=1
        csv_writer.writerow(d.values())
    O_file.close()


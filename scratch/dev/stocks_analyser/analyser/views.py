from django.shortcuts import render,redirect
from sqlalchemy import create_engine
import pandas as pd
from .models import Equity_Files
from django.db import connections
import datetime as dt
# Create your views here.


def analyser(request):
    return render(request,"base/base.html")

def upload(request):
    return render(request,'analyser/upload.html')

def equity(request):
    return render(request,'analyser/equity_analyser.html')

def equity_file_upload_v1(request):
    """Upload file with predefined columns"""
    if request.method=="POST" and request.FILES["file"]:
        file=request.FILES["file"]
        equity_file_name=request.POST.get("equity_file_name")
        print(file)
        df=pd.read_csv(file)
        df['username']=request.user.username
        df['equity_file_name']=equity_file_name
        print(df)
        df.to_sql(Equity_Files,con=sql_conn(),if_exists="append", index=False)
    return render(request, 'analyser/upload.html')

def equity_file_upload_v2(request):
    """Upload file with predefined columns"""
    if request.method == 'POST' and request.FILES.get('file'):
        file=request.FILES["file"]
        equity_file_name=request.POST.get("equity_file_name")
        print(file)
        df=pd.read_csv(file)
        print(df)
        df.insert(0,"username",value=request.user.username)
        df.insert(1,"datetime",value=dt.datetime.now())
        df.insert(2,"equity_file_name",value=equity_file_name)
        handle_uploaded_csv_v1(df)
        # Redirect to a success page or another view
    return render(request, 'analyser/upload.html')

def handle_uploaded_csv_v1(df):
    print("\nadded df\n",df)
    df.fillna(0.0, inplace=True)
    list_of_rows=[list(row) for row in df.values]
    for i in list_of_rows:
        Equity_Files.objects.create(
            #column1=i[0],
            #column2=row['column2'],
            username=i[0],
            datetime=i[1],
            equity_file_name=i[2],
            name=i[3],
            bse_code=i[4],
            nse_code=i[5],
            industry=i[6],
            current_price=i[7],
            market_capitalization=i[8],
            price_to_earning=i[9],
            industry_pe=i[10],
            eps=i[11],
            # Add more fields as needed
        )

def handle_uploaded_csv(df):
    # Process the CSV file using pandas and save data to the database
    engine = connections['default'].connection
    df.to_sql(Equity_Files, if_exists='append', index=False, con=engine)

def equity_files(request):
    username=request.user.username
    try:
        print("trying..")
        equity_files_names=Equity_Files.objects.filter(username=username).values()
        equity_files_names=pd.DataFrame(equity_files_names)[['equity_file_name','datetime']].drop_duplicates().sort_values(by="datetime",ascending=False).reset_index()
        equity_files_names.index+=1
        equity_files_names.rename(columns={"index":"Sr No"})
        print(equity_files_names)
        context={"equity_files_names":equity_files_names}
    except:
        print("excepted..")
        equity_files_names=pd.DataFrame()
        print(equity_files_names)
        context={"equity_files_names":equity_files_names}
    return render(request,'analyser/equity_files.html',context=context)

def equity_view_file(request,equity_file_name):
    equity_file_df = Equity_Files.objects.filter(equity_file_name=equity_file_name).values()
    equity_file_df=pd.DataFrame(equity_file_df)
    file_name=equity_file_name
    file_datetime=equity_file_df['datetime'].iloc[0]
    equity_file_df=equity_file_df.drop(columns=["username","datetime","equity_file_name"])
    print(equity_file_df,file_datetime)
    return render(request, 'analyser/equity_files_show.html', {'equity_file_df': equity_file_df.to_html(classes='pandas_table', index=False,escape=False),'equity_file_name':file_name,'equity_file_datetime':file_datetime,'file_length':len(equity_file_df)})
  
def delete_equity_file(request, equity_file_name):
    item = get_object_or_404(Equity_Files, equity_file_name=equity_file_name)
    print(item)
    item.delete()
    return redirect('equity')

def equity_filter(request):
    equity_files_names=Equity_Files.objects.filter(username=request.user.username).values()
    equity_files_names=pd.DataFrame(equity_files_names)[['equity_file_name','datetime']].drop_duplicates().sort_values(by="datetime",ascending=False).reset_index()
    equity_files_names.index+=1
    equity_files_names.rename(columns={"index":"Sr No"})
    equity_files_names=equity_files_names['equity_file_name'].to_list()
    context={"equity_files_names":equity_files_names}
    return render(request,'analyser/equity_filter.html',context=context)

def equity_file_select(request):
    if request.method=="POST":
        
        equity_files_names=Equity_Files.objects.filter(username=request.user.username).values()
        equity_files_names=pd.DataFrame(equity_files_names)[['equity_file_name','datetime']].drop_duplicates().sort_values(by="datetime",ascending=False).reset_index()
        equity_files_names.index+=1
        equity_files_names.rename(columns={"index":"Sr No"})
        equity_files_names=equity_files_names['equity_file_name'].to_list()
     
        selected_equity_file_name=request.POST.get("selected_equity_file_name")

        equity_file_df = Equity_Files.objects.filter(equity_file_name=selected_equity_file_name).values()
        equity_file_df=pd.DataFrame(equity_file_df)
        equity_files_parameters_names=equity_file_df.drop(columns=["username","datetime","equity_file_name"]).columns.to_list()
        request.session['equity_files_parameters_names']=equity_files_parameters_names
        print(request.session['equity_files_parameters_names'])
        context={"equity_files_names":equity_files_names,"equity_files_parameter_names":equity_files_parameters_names}
    return render(request,'analyser/equity_create_filter.html',context=context)

def equity_create_filer(request):

    equity_files_names=Equity_Files.objects.filter(username=request.user.username).values()
    equity_files_names=pd.DataFrame(equity_files_names)[['equity_file_name','datetime']].drop_duplicates().sort_values(by="datetime",ascending=False).reset_index()
    equity_files_names.index+=1
    equity_files_names.rename(columns={"index":"Sr No"})
    equity_files_names=equity_files_names['equity_file_name'].to_list()

    context={"equity_files_names":equity_files_names}
    return render(request,'analyser/equity_create_filter.html',context=context)

def get_session_equity_parameters(request):
    # Retrieve the serialized DataFrame from session
    equity_files_parameters_names = request.session.get('equity_files_parameters_names')
    print(equity_files_parameters_names)
    # If the DataFrame exists in session, deserialize it; otherwise, create a new DataFrame
    if equity_files_parameters_names:
        df = equity_files_parameters_names
    else:
        df = []  # Adjust column names as needed

    return df

def equity_analyser(request):
    return redirect('equity')

def get_session_dataframe(request):
    # Retrieve the serialized DataFrame from session
    serialized_dataframe = request.session.get('temp_df')

    # If the DataFrame exists in session, deserialize it; otherwise, create a new DataFrame
    if serialized_dataframe:
        df = pd.read_json(serialized_dataframe)
    else:
        df = pd.DataFrame()  # Adjust column names as needed

    return df

def store_session_dataframe(request, df):
    # Serialize the DataFrame and store it in session
    serialized_dataframe = df.to_json()
    request.session['temp_df'] = serialized_dataframe

def equity_create_filer_temp_store(request):
    # Step 1: Retrieve DataFrame from session
    if request.method=="POST":
        form_data = {key: request.POST[key] for key in request.POST}
        # Assuming you have a DataFrame named 'df'
        print(form_data)
        df = get_session_dataframe(request)

        # Step 2: Add extra rows (modify DataFrame as needed)
        #new_rows = {'Column1': ['NewValue1', 'NewValue2'], 'Column2': ['NewValue3', 'NewValue4']}
        df=pd.concat([df,pd.DataFrame([form_data])],ignore_index=True,)

        #df = df.append(pd.DataFrame(form_data), ignore_index=True)
        print(df)
        # Step 3: Update session with modified DataFrame
        store_session_dataframe(request, df)
        param_list=get_session_equity_parameters(request)
        context={"temp_df":df.drop('csrfmiddlewaretoken',axis=1).to_html(classes='pandas_table', index=False,escape=False),"equity_files_parameter_names":param_list}
        return render(request,'analyser/equity_create_filter.html',context = context)

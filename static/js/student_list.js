function searchId(){
    var input,table,tr,td,filter,i,txtData;
    input=document.getElementById('form1');
    filter=input.value.toUpperCase();
    table=document.getElementById('table1');
    tr=table.getElementsByTagName('tr');
    for(i=0;i<tr.length;i++){
        if(tr[i].id!=="head"){
      td=tr[i].getElementsByTagName('td');
      console.log(td)
      for(x in td){
      if(td[x]){
           txtData=td[x].innerText;
           if(txtData!==undefined && txtData.toUpperCase().indexOf(filter)>-1){
               tr[i].style.display="";
               break;
           }
           else{
               if(txtData!=="studentId"){
              tr[i].style.display="none";}
           }
      }
    }
}
    }
}
function searchByDiv(e){
    console.log(e)
    var input,table,tr,td,filter,i,txtData;
    input=document.getElementById('form1');
    filter=e.target.value;
    table=document.getElementById('table1');
    tr=table.getElementsByTagName('tr');
    for(i=0;i<tr.length;i++){
        if(tr[i].id!=="head"){
      td=tr[i].getElementsByTagName('td');
      console.log(td)
      
      if(td[2]){
           txtData=td[2].innerText;
           if(txtData!==undefined && txtData.toUpperCase().indexOf(filter)>-1){
               tr[i].style.display="";
               
           }
           else{
               if(txtData!=="studentId"){
              tr[i].style.display="none";}
           }
      }
    
}
    }
}
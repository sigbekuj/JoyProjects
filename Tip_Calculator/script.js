bill_amount = prompt("Enter your total bill");

if (!isNaN(bill_amount)){
    tip_percentage = prompt("Choose a tip percentage you would like to give: 10%,15% etc");
}else{
    alert("invalid number try again")
        
}
    

total_tip = (tip_percentage/100)*bill_amount ;
console.log(`Your total tip is ${total_tip}`); 

total_amount = bill_amount + total_tip ;
console.log(`Your full amount is ${total_amount}`);
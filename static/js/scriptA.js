function incrementar() {
valor = document.getElementById("id_cantidad");
extra = document.getElementById("id_cebolla")
if(extra==null){
extra=0;
}
valor.value++;
}
function decrementar() {
valor = document.getElementById("id_cantidad");
cond = document.getElementById("id_cebolla");
if (valor.value>=2)valor.value--;
if (cond.value>valor.value)cond.value=valor.value;
}
function incrementar1() {
total=document.getElementById("id_cantidad");
valor = document.getElementById("id_cebolla");
if(total.value>valor.value){
valor.value++;
}}
function decrementar1() {
valor = document.getElementById("id_cebolla");
if (valor.value>=1)
valor.value--;
}
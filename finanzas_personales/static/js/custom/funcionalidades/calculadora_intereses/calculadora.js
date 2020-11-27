var cantidad = $("#cantidad")
var cuotas = $("#cuotas")
var tasa_interes = $("#tasa_interes")

cantidad.keyup(function() {
    valor = $(this).val().replaceAll(',','')
    if (valor){                            
        humanize = Humanize.intComma(parseInt(valor))
        $(this).val(humanize)
    }
    validacion_valores();            
})
cuotas.keyup(function() {
    validacion_valores();
})
tasa_interes.keyup(function() {
    validacion_valores();
})

function validacion_valores(){            
    if (cantidad.val() && cuotas.val() && tasa_interes.val()){
        $("#container-results").show()
        cantidad_val = parseFloat(cantidad.val().replaceAll(',',''))
        cuotas_val = parseInt(cuotas.val())
        tasa_interes_val = parseFloat(tasa_interes.val())/100
        let interes = (cantidad_val*tasa_interes_val)
        total = Humanize.intComma((cantidad_val/cuotas_val)+interes, 2)

        monthly_fee = $("#monthly_fee_value")
        monthly_fee.text(`$ ${total}`)
        resumen_datos(cantidad_val, total, cuotas_val, interes)
    }else{
        $("#container-results").hide()
    }
}

function resumen_datos(cantidad_original, total_pagar, cuotas_totales, interes){
    let total_payment = $("#total_payment")
    let interests = $("#interests")
    let amount = $("#amount")
    let increase = $("#increase")            
    let total_intereses = parseInt(total_pagar.replaceAll(',',''))*cuotas_totales
    let incremento = Humanize.intComma(((total_intereses/cantidad_original)-1)*100, 2)
    
    total_payment.text(`$ ${Humanize.intComma(total_intereses, 2)}`)
    interests.text(`$ ${Humanize.intComma(interes*cuotas_totales, 2)}`)
    amount.text(`$ ${Humanize.intComma(cantidad_original, 2)}`)
    increase.text(`${incremento}%`)

}
$(document).ready(function() {
    $("#container-results").hide()
})
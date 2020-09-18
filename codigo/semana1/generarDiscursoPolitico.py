import random

labetazo = ['QUERIDOS','APRECIADOS','DISTINGUIDOS','HONORABLES','ESTIMADOS','RESPETADOS']
marrano = ['COMPATRIOTAS','CONCIUDADANOS','AMIGOS','COTERRANEOS','COPARTIDARIOS','ELECTORES']
condicion = ['EN MI GOBIERNO','CON SU APOYO','SIENDO ELEGIDO','CON SU AYUDA','SI ME SIGUEN','DURANTE MI MANDATO']
compromiso = ['COMBATIRÉ','LUCHARÉ CONTRA','ACABARÉ','ELIMINARÉ','VENCERÉ','VOY A DERROTAR']
ilusion = ['LA VIOLENCIA Y','LA DELINCUENCIA Y','LA CORRUPCIÓN Y','LA INFLACIÓN Y','LA POBREZA Y','EL DESPLAZAMIENTO Y']
promesa = ['DEFENDERÉ','PROMOVERÉ','VELARÉ POR','PROTEGERÉ','GARANTIZARÉ','TRABAJARÉ POR']
beneficio = ['LA EDUCACIÓN','EL EMPLEO','LA SEGURIDAD','LA LAZ','LA IGUALDAD','LA SALUD']
cantidad_votos = ['DE LA COMUNIDAD','DE LA CIUDAD','DEL PAÍS','DE LA POBLACIÓN','PARA TODA LA GENTE','DE CADA COLOMBIANO']

labetazo_select = random.choice(labetazo)
marrano_select = random.choice(marrano)
condicion_select = random.choice(condicion)
compromiso_select = random.choice(compromiso)
ilusion_select = random.choice(ilusion)
promesa_select = random.choice(promesa)
beneficio_select = random.choice(beneficio)
cantidad_votos_select = random.choice(cantidad_votos)

print(f'El discurso resultante es: {labetazo_select} {marrano_select} {condicion_select} {compromiso_select} {ilusion_select} {promesa_select} {beneficio_select} {cantidad_votos_select}')
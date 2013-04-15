class MaquinaVirtual:
  cuadruplos = []

	_cont_int_glo = []
	_cont_flo_glo = []
	_cont_dou_glo = []
	_cont_str_glo = []
	_cont_bool_glo = []
	_cont_list_glo = []
	_cont_arr_glo = []

	_cont_int_loc = []
	_cont_flo_loc = []
	_cont_dou_loc = []
	_cont_str_loc = []
	_cont_bool_loc = []
	_cont_list_loc = []
	_cont_arr_loc = []

	_cont_int_tmp = []
	_cont_flo_tmp = []
	_cont_dou_tmp = []
	_cont_str_tmp = []
	_cont_bool_tmp = []
	_cont_list_tmp = []
	_cont_arr_tmp = []

	_cont_int_cons = []
	_cont_flo_cons = []
	_cont_dou_cons = []
	_cont_str_cons = []
	_cont_bool_cons = []
	_cont_list_cons = []
	_cont_arr_cons = []

	_procedimientos = []

	_apuntador_inst = [] # Apunta a la posicion del arreglo de instrucciones para ejecutar el cuadruplo
	_apuntador = 0 # Apunta a la posicion del arreglo de instrucciones para ejecutar el cuadruplo

	_offsets = [int()] * 14
	_before = [int()] * 14
	_enable_offsets = bool()
	_use_before_offsets_values = bool()
	_procedimiento_actual = []

	# Inicializa maquina virtual
	## Revisar si lo que se busca es hacer referencia a las variables de instancia
	## o a las variables de clase "self"
	def __init__(self):
		_apuntador_inst = [0] * 1000
		_offsets = [0] * 14
		_apuntador = 0
		_enable_offsets = False
		_use_before_offsets_values = False

	def ejecutar(self):
		_procedimiento_actual.push("Start")
		carga_proc(_procedimiento_actual[len(_procedimiento_actual)-1])
		while True:
			comando = cuadruplos[_apuntador_inst[_apuntador]].op
			direccion_var1 = 0
			if comando != "ERA" and comando != "param":
				direccion_var1 = cuadruplos[_apuntador_inst[_apuntador]].o1
			direccion_var2 = cuadruplos[_apuntador_inst[_apuntador]].o2
			direccion_dest = cuadruplos[_apuntador_inst[_apuntador]].res 
			val1 = [""] * 2
			val2 = [""] * 2
			if (comando == "+" or comando == "-" or comando == "*" or comando == "/") or 
			(direccion_var1 != 0 and comando != "goto" and comando != "ERA" and comando != "param"):
				if _use_before_offsets_values:
					valores1 = get_valor(direccion_var1, _before)
				else:
					valores1 = get_valor(direccion_var1, _offsets)
			if (comando == "+" or comando == "-" or comando == "*" or comando == "/") or 
			(direccion_var2 != 0 and comando != "goto" and comando != "ERA" and comando != "param"):
				if _use_before_offsets_values:
					valores2 = get_valor(direccion_var2, _before)
				else:
					valores2 = get_valor(direccion_var2, _offsets)

			if comando == "+":
				if in_range(direccion_dest, 0, 7000):
					if in_range(direccion_dest, 0, 1000):
						if valores1[1] == "Integer" or valores1[1] == "Float" or valores1[1] == "Double":
							if valores2[1] == "Integer" or valores2[1] == "Float" or valores2[1] == "Double":
								_cont_int_glo[direccion_dest].valor = int(valores1[0]) + int(valores2[0])
							else:
								# Error: el valor tiene que ser entero 															
						else:
							# Error
					elif in_range(direccion_dest, 1000, 2000):
						direccion_dest -= 1000
						if valores1[1] == "Integer" or valores1[1] == "Float" or valores1[1] == "Double":
							if valores2[1] == "Integer" or valores2[1] == "Float" or valores2[1] == "Double":
								_cont_flo_glo[direccion_dest].valor = float(valores1[0]) + float(valores2[0])
							else:
								# Error
						else:
							# Error
					elif in_range(direccion_dest, 2000, 3000):
						direccion_dest -= 2000
						if valores1[1] == "Integer" or valores1[1] == "Float" or valores1[1] == "Double":
							if valores2[1] == "Integer" or valores2[1] == "Float" or valores2[1] == "Double":
								_cont_dou_glo[direccion_dest].valor = float(valores1[0]) + float(valores2[0])
							else:
								# Error
						else:
							# Error
					elif in_range(direccion_dest, 3000, 4000):
						direccion_dest -= 3000
						if valores1[1] == "String":
							if valores2[1] == "String":
								_cont_str_glo[direccion_dest].valor = str(valores1[0]) + str(valores2[0])
							else:
								# Error
						else:
							# Error
					elif in_range(direccion_dest, 4000, 5000):
						direccion_dest -= 4000
					elif in_range(direccion_dest, 5000, 6000):
						direccion_dest -= 5000
						if valores1[1] == "List":
							if valores2[1] == "List":
								_cont_list_glo[direccion_dest].valor = list(valores1[0]) + list(valores2[0])
							else:
								# Error
						else:
							# Error
					elif in_range(direccion_dest, 6000, 7000):
						direccion_dest -= 6000
						if valores1[1] == "Array":
							if valores2[1] == "Array":
								_cont_arr_glo[direccion_dest].valor = list(valores1[0]) + list(valores2[0])
							else:
								# Error
						else:
							# Error
				elif in_range(direccion_dest, 7000, 14000):
					direccion_dest -= 7000
					if in_range(direccion_dest, 0, 1000):
						if valores1[1] == "Integer" or valores1[1] == "Float" or valores1[1] == "Double":
							if valores2[1] == "Integer" or valores2[1] == "Float" or valores2[1] == "Double":
								if _use_before_offsets_values:
									_cont_int_loc[direccion_dest+(_before[0] if _enable_offsets else 0)].valor = int(valores1[0]) + int(valores2[0])
								else:
									_cont_int_loc[direccion_dest+(_offsets[0] if _enable_offsets else 0)].valor = int(valores1[0]) + int(valores2[0])
							else:
								# Error: el valor tiene que ser entero 
						else:
							# Error
					elif in_range(direccion_dest, 1000, 2000):
						direccion_dest -= 1000
						if valores1[1] == "Integer" or valores1[1] == "Float" or valores1[1] == "Double":
							if valores2[1] == "Integer" or valores2[1] == "Float" or valores2[1] == "Double":
								if _use_before_offsets_values:
									_cont_flo_loc[direccion_dest+(_before[1] if _enable_offsets else 0)].valor = float(valores1[0]) + float(valores2[0])
								else:
									_cont_flo_loc[direccion_dest+(_offsets[1] if _enable_offsets else 0)].valor = float(valores1[0]) + float(valores2[0])
							else:
								# Error
						else:
							# Error
					elif in_range(direccion_dest, 2000, 3000):
						direccion_dest -= 2000
						if valores1[1] == "Integer" or valores1[1] == "Float" or valores1[1] == "Double":
							if valores2[1] == "Integer" or valores2[1] == "Float" or valores2[1] == "Double":
								if _use_before_offsets_values:
									_cont_dou_loc[direccion_dest+(_before[2] if _enable_offsets else 0)].valor = float(valores1[0]) + float(valores2[0])
								else:
									_cont_dou_loc[direccion_dest+(_offsets[2] if _enable_offsets else 0)].valor = float(valores1[0]) + float(valores2[0])
							else:
								# Error
						else:
							# Error
					elif in_range(direccion_dest, 3000, 4000):
						direccion_dest -= 3000
						if valores1[1] == "String":
							if valores2[1] == "String":
								if _use_before_offsets_values:
									_cont_str_loc[direccion_dest+(_before[3] if _enable_offsets else 0)].valor = str(valores1[0]) + str(valores2[0])
								else:
									_cont_dou_loc[direccion_dest+(_offsets[3] if _enable_offsets else 0)].valor = str(valores1[0]) + str(valores2[0])
							else:
								# Error
						else:
							# Error
					elif in_range(direccion_dest, 4000, 5000):
						direccion_dest -= 4000
					elif in_range(direccion_dest, 5000, 6000):
						direccion_dest -= 5000
						if valores1[1] == "List":
							if valores2[1] == "List":
							if _use_before_offsets_values:
									_cont_list_loc[direccion_dest+(_before[5] if _enable_offsets else 0)].valor = list(valores1[0]) + list(valores2[0])
								else:
									_cont_list_loc[direccion_dest+(_offsets[5] if _enable_offsets else 0)].valor = list(valores1[0]) + list(valores2[0])
							else:
								# Error
						else:
							# Error
					elif in_range(direccion_dest, 6000, 7000):
						direccion_dest -= 6000
						if valores1[1] == "Array":
							if valores2[1] == "Array":
							if _use_before_offsets_values:
									_cont_arr_loc[direccion_dest+(_before[6] if _enable_offsets else 0)].valor = list(valores1[0]) + list(valores2[0])
								else:
									_cont_arr_loc[direccion_dest+(_offsets[6] if _enable_offsets else 0)].valor = list(valores1[0]) + list(valores2[0])
							else:
								# Error
						else:
							# Error
				elif in_range(direccion_dest, 14000, 21000):
					direccion_dest -= 14000
					if in_range(direccion_dest, 0, 1000):
						if valores1[1] == "Integer" or valores1[1] == "Float" or valores1[1] == "Double":
							if valores2[1] == "Integer" or valores2[1] == "Float" or valores2[1] == "Double":
								if _use_before_offsets_values:
									_cont_int_tmp[direccion_dest+(_before[7] if _enable_offsets else 0)].valor = int(valores1[0]) + int(valores2[0])
								else:
									_cont_int_tmp[direccion_dest+(_offsets[7] if _enable_offsets else 0)].valor = int(valores1[0]) + int(valores2[0])
							else:
								# Error: el valor tiene que ser entero 
						else:
							# Error
					elif in_range(direccion_dest, 1000, 2000):
						direccion_dest -= 1000
						if valores1[1] == "Integer" or valores1[1] == "Float" or valores1[1] == "Double":
							if valores2[1] == "Integer" or valores2[1] == "Float" or valores2[1] == "Double":
								if _use_before_offsets_values:
									_cont_flo_tmp[direccion_dest+(_before[8] if _enable_offsets else 0)].valor = float(valores1[0]) + float(valores2[0])
								else:
									_cont_flo_tmp[direccion_dest+(_offsets[8] if _enable_offsets else 0)].valor = float(valores1[0]) + float(valores2[0])
							else:
								# Error
						else:
							# Error
					elif in_range(direccion_dest, 2000, 3000):
						direccion_dest -= 2000
						if valores1[1] == "Integer" or valores1[1] == "Float" or valores1[1] == "Double":
							if valores2[1] == "Integer" or valores2[1] == "Float" or valores2[1] == "Double":
								if _use_before_offsets_values:
									_cont_dou_tmp[direccion_dest+(_before[9] if _enable_offsets else 0)].valor = float(valores1[0]) + float(valores2[0])
								else:
									_cont_dou_tmp[direccion_dest+(_offsets[9] if _enable_offsets else 0)].valor = float(valores1[0]) + float(valores2[0])
							else:
								# Error
						else:
							# Error
					elif in_range(direccion_dest, 3000, 4000):
						direccion_dest -= 3000
						if valores1[1] == "String":
							if valores2[1] == "String":
								if _use_before_offsets_values:
									_cont_str_tmp[direccion_dest+(_before[10] if _enable_offsets else 0)].valor = str(valores1[0]) + str(valores2[0])
								else:
									_cont_dou_tmp[direccion_dest+(_offsets[10] if _enable_offsets else 0)].valor = str(valores1[0]) + str(valores2[0])
							else:
								# Error
						else:
							# Error
					elif in_range(direccion_dest, 4000, 5000):
						direccion_dest -= 4000
					elif in_range(direccion_dest, 5000, 6000):
						direccion_dest -= 5000
						if valores1[1] == "List":
							if valores2[1] == "List":
							if _use_before_offsets_values:
									_cont_list_tmp[direccion_dest+(_before[12] if _enable_offsets else 0)].valor = list(valores1[0]) + list(valores2[0])
								else:
									_cont_list_tmp[direccion_dest+(_offsets[12] if _enable_offsets else 0)].valor = list(valores1[0]) + list(valores2[0])
							else:
								# Error
						else:
							# Error
					elif in_range(direccion_dest, 6000, 7000):
						direccion_dest -= 6000
						if valores1[1] == "Array":
							if valores2[1] == "Array":
							if _use_before_offsets_values:
									_cont_arr_tmp[direccion_dest+(_before[13] if _enable_offsets else 0)].valor = list(valores1[0]) + list(valores2[0])
								else:
									_cont_arr_tmp[direccion_dest+(_offsets[13] if _enable_offsets else 0)].valor = list(valores1[0]) + list(valores2[0])
							else:
								# Error
						else:
							# Error
				else:
					direccion_dest -= 21000
					if in_range(direccion_dest, 0, 1000):
						if valores1[1] == "Integer" or valores1[1] == "Float" or valores1[1] == "Double":
							if valores2[1] == "Integer" or valores2[1] == "Float" or valores2[1] == "Double":
								_cont_int_cons[direccion_dest].valor = int(valores1[0]) + int(valores2[0])
							else:
								# Error: el valor tiene que ser entero 															
						else:
							# Error
					elif in_range(direccion_dest, 1000, 2000):
						direccion_dest -= 1000
						if valores1[1] == "Integer" or valores1[1] == "Float" or valores1[1] == "Double":
							if valores2[1] == "Integer" or valores2[1] == "Float" or valores2[1] == "Double":
								_cont_flo_cons[direccion_dest].valor = float(valores1[0]) + float(valores2[0])
							else:
								# Error
						else:
							# Error
					elif in_range(direccion_dest, 2000, 3000):
						direccion_dest -= 2000
						if valores1[1] == "Integer" or valores1[1] == "Float" or valores1[1] == "Double":
							if valores2[1] == "Integer" or valores2[1] == "Float" or valores2[1] == "Double":
								_cont_dou_cons[direccion_dest].valor = float(valores1[0]) + float(valores2[0])
							else:
								# Error
						else:
							# Error
					elif in_range(direccion_dest, 3000, 4000):
						direccion_dest -= 3000
						if valores1[1] == "String":
							if valores2[1] == "String":
								_cont_str_cons[direccion_dest].valor = str(valores1[0]) + str(valores2[0])
							else:
								# Error
						else:
							# Error
					elif in_range(direccion_dest, 4000, 5000):
						direccion_dest -= 4000
					elif in_range(direccion_dest, 5000, 6000):
						direccion_dest -= 5000
						if valores1[1] == "List":
							if valores2[1] == "List":
								_cont_list_cons[direccion_dest].valor = list(valores1[0]) + list(valores2[0])
							else:
								# Error
						else:
							# Error
					elif in_range(direccion_dest, 6000, 7000):
						direccion_dest -= 6000
						if valores1[1] == "Array":
							if valores2[1] == "Array":
								_cont_arr_cons[direccion_dest].valor = list(valores1[0]) + list(valores2[0])
							else:
								# Error
						else:
							# Error
			if comando == "-":
				if in_range(direccion_dest, 0, 7000):
					if in_range(direccion_dest, 0, 1000):
						if valores1[1] == "Integer" or valores1[1] == "Float" or valores1[1] == "Double":
							if valores2[1] == "Integer" or valores2[1] == "Float" or valores2[1] == "Double":
								_cont_int_glo[direccion_dest].valor = int(valores1[0]) - int(valores2[0])
							else:
								# Error: el valor tiene que ser entero 															
						else:
							# Error
					elif in_range(direccion_dest, 1000, 2000):
						direccion_dest -= 1000
						if valores1[1] == "Integer" or valores1[1] == "Float" or valores1[1] == "Double":
							if valores2[1] == "Integer" or valores2[1] == "Float" or valores2[1] == "Double":
								_cont_flo_glo[direccion_dest].valor = float(valores1[0]) - float(valores2[0])
							else:
								# Error
						else:
							# Error
					elif in_range(direccion_dest, 2000, 3000):
						direccion_dest -= 2000
						if valores1[1] == "Integer" or valores1[1] == "Float" or valores1[1] == "Double":
							if valores2[1] == "Integer" or valores2[1] == "Float" or valores2[1] == "Double":
								_cont_dou_glo[direccion_dest].valor = float(valores1[0]) - float(valores2[0])
							else:
								# Error
						else:
							# Error
					elif in_range(direccion_dest, 3000, 4000):
						direccion_dest -= 3000
					elif in_range(direccion_dest, 4000, 5000):
						direccion_dest -= 4000
					elif in_range(direccion_dest, 5000, 6000):
						direccion_dest -= 5000
					elif in_range(direccion_dest, 6000, 7000):
						direccion_dest -= 6000
				elif in_range(direccion_dest, 7000, 14000):
					direccion_dest -= 7000
					if in_range(direccion_dest, 0, 1000):
						if valores1[1] == "Integer" or valores1[1] == "Float" or valores1[1] == "Double":
							if valores2[1] == "Integer" or valores2[1] == "Float" or valores2[1] == "Double":
								if _use_before_offsets_values:
									_cont_int_loc[direccion_dest+(_before[0] if _enable_offsets else 0)].valor = int(valores1[0]) - int(valores2[0])
								else:
									_cont_int_loc[direccion_dest+(_offsets[0] if _enable_offsets else 0)].valor = int(valores1[0]) - int(valores2[0])
							else:
								# Error: el valor tiene que ser entero 
						else:
							# Error
					elif in_range(direccion_dest, 1000, 2000):
						direccion_dest -= 1000
						if valores1[1] == "Integer" or valores1[1] == "Float" or valores1[1] == "Double":
							if valores2[1] == "Integer" or valores2[1] == "Float" or valores2[1] == "Double":
								if _use_before_offsets_values:
									_cont_flo_loc[direccion_dest+(_before[1] if _enable_offsets else 0)].valor = float(valores1[0]) - float(valores2[0])
								else:
									_cont_flo_loc[direccion_dest+(_offsets[1] if _enable_offsets else 0)].valor = float(valores1[0]) - float(valores2[0])
							else:
								# Error
						else:
							# Error
					elif in_range(direccion_dest, 2000, 3000):
						direccion_dest -= 2000
						if valores1[1] == "Integer" or valores1[1] == "Float" or valores1[1] == "Double":
							if valores2[1] == "Integer" or valores2[1] == "Float" or valores2[1] == "Double":
								if _use_before_offsets_values:
									_cont_dou_loc[direccion_dest+(_before[2] if _enable_offsets else 0)].valor = float(valores1[0]) - float(valores2[0])
								else:
									_cont_dou_loc[direccion_dest+(_offsets[2] if _enable_offsets else 0)].valor = float(valores1[0]) - float(valores2[0])
							else:
								# Error
						else:
							# Error
					elif in_range(direccion_dest, 3000, 4000):
						direccion_dest -= 3000
					elif in_range(direccion_dest, 4000, 5000):
						direccion_dest -= 4000
					elif in_range(direccion_dest, 5000, 6000):
						direccion_dest -= 5000
					elif in_range(direccion_dest, 6000, 7000):
						direccion_dest -= 6000
				elif in_range(direccion_dest, 14000, 21000):
					direccion_dest -= 14000
					if in_range(direccion_dest, 0, 1000):
						if valores1[1] == "Integer" or valores1[1] == "Float" or valores1[1] == "Double":
							if valores2[1] == "Integer" or valores2[1] == "Float" or valores2[1] == "Double":
								if _use_before_offsets_values:
									_cont_int_tmp[direccion_dest+(_before[7] if _enable_offsets else 0)].valor = int(valores1[0]) - int(valores2[0])
								else:
									_cont_int_tmp[direccion_dest+(_offsets[7] if _enable_offsets else 0)].valor = int(valores1[0]) - int(valores2[0])
							else:
								# Error: el valor tiene que ser entero 
						else:
							# Error
					elif in_range(direccion_dest, 1000, 2000):
						direccion_dest -= 1000
						if valores1[1] == "Integer" or valores1[1] == "Float" or valores1[1] == "Double":
							if valores2[1] == "Integer" or valores2[1] == "Float" or valores2[1] == "Double":
								if _use_before_offsets_values:
									_cont_flo_tmp[direccion_dest+(_before[8] if _enable_offsets else 0)].valor = float(valores1[0]) - float(valores2[0])
								else:
									_cont_flo_tmp[direccion_dest+(_offsets[8] if _enable_offsets else 0)].valor = float(valores1[0]) - float(valores2[0])
							else:
								# Error
						else:
							# Error
					elif in_range(direccion_dest, 2000, 3000):
						direccion_dest -= 2000
						if valores1[1] == "Integer" or valores1[1] == "Float" or valores1[1] == "Double":
							if valores2[1] == "Integer" or valores2[1] == "Float" or valores2[1] == "Double":
								if _use_before_offsets_values:
									_cont_dou_tmp[direccion_dest+(_before[9] if _enable_offsets else 0)].valor = float(valores1[0]) - float(valores2[0])
								else:
									_cont_dou_tmp[direccion_dest+(_offsets[9] if _enable_offsets else 0)].valor = float(valores1[0]) - float(valores2[0])
							else:
								# Error
						else:
							# Error
					elif in_range(direccion_dest, 3000, 4000):
						direccion_dest -= 3000
					elif in_range(direccion_dest, 4000, 5000):
						direccion_dest -= 4000
					elif in_range(direccion_dest, 5000, 6000):
						direccion_dest -= 5000
					elif in_range(direccion_dest, 6000, 7000):
						direccion_dest -= 6000
				else:
					direccion_dest -= 21000
					if in_range(direccion_dest, 0, 1000):
						if valores1[1] == "Integer" or valores1[1] == "Float" or valores1[1] == "Double":
							if valores2[1] == "Integer" or valores2[1] == "Float" or valores2[1] == "Double":
								_cont_int_cons[direccion_dest].valor = int(valores1[0]) - int(valores2[0])
							else:
								# Error: el valor tiene que ser entero 															
						else:
							# Error
					elif in_range(direccion_dest, 1000, 2000):
						direccion_dest -= 1000
						if valores1[1] == "Integer" or valores1[1] == "Float" or valores1[1] == "Double":
							if valores2[1] == "Integer" or valores2[1] == "Float" or valores2[1] == "Double":
								_cont_flo_cons[direccion_dest].valor = float(valores1[0]) - float(valores2[0])
							else:
								# Error
						else:
							# Error
					elif in_range(direccion_dest, 2000, 3000):
						direccion_dest -= 2000
						if valores1[1] == "Integer" or valores1[1] == "Float" or valores1[1] == "Double":
							if valores2[1] == "Integer" or valores2[1] == "Float" or valores2[1] == "Double":
								_cont_dou_cons[direccion_dest].valor = float(valores1[0]) - float(valores2[0])
							else:
								# Error
						else:
							# Error
					elif in_range(direccion_dest, 3000, 4000):
						direccion_dest -= 3000
					elif in_range(direccion_dest, 4000, 5000):
						direccion_dest -= 4000
					elif in_range(direccion_dest, 5000, 6000):
						direccion_dest -= 5000
					elif in_range(direccion_dest, 6000, 7000):
						direccion_dest -= 6000
			if comando == "*":
				if in_range(direccion_dest, 0, 7000):
					if in_range(direccion_dest, 0, 1000):
						if valores1[1] == "Integer" or valores1[1] == "Float" or valores1[1] == "Double":
							if valores2[1] == "Integer" or valores2[1] == "Float" or valores2[1] == "Double":
								_cont_int_glo[direccion_dest].valor = int(valores1[0]) * int(valores2[0])
							else:
								# Error: el valor tiene que ser entero 															
						else:
							# Error
					elif in_range(direccion_dest, 1000, 2000):
						direccion_dest -= 1000
						if valores1[1] == "Integer" or valores1[1] == "Float" or valores1[1] == "Double":
							if valores2[1] == "Integer" or valores2[1] == "Float" or valores2[1] == "Double":
								_cont_flo_glo[direccion_dest].valor = float(valores1[0]) * float(valores2[0])
							else:
								# Error
						else:
							# Error
					elif in_range(direccion_dest, 2000, 3000):
						direccion_dest -= 2000
						if valores1[1] == "Integer" or valores1[1] == "Float" or valores1[1] == "Double":
							if valores2[1] == "Integer" or valores2[1] == "Float" or valores2[1] == "Double":
								_cont_dou_glo[direccion_dest].valor = float(valores1[0]) * float(valores2[0])
							else:
								# Error
						else:
							# Error
					elif in_range(direccion_dest, 3000, 4000):
						direccion_dest -= 3000
					elif in_range(direccion_dest, 4000, 5000):
						direccion_dest -= 4000
					elif in_range(direccion_dest, 5000, 6000):
						direccion_dest -= 5000
					elif in_range(direccion_dest, 6000, 7000):
						direccion_dest -= 6000
				elif in_range(direccion_dest, 7000, 14000):
					direccion_dest -= 7000
					if in_range(direccion_dest, 0, 1000):
						if valores1[1] == "Integer" or valores1[1] == "Float" or valores1[1] == "Double":
							if valores2[1] == "Integer" or valores2[1] == "Float" or valores2[1] == "Double":
								if _use_before_offsets_values:
									_cont_int_loc[direccion_dest+(_before[0] if _enable_offsets else 0)].valor = int(valores1[0]) * int(valores2[0])
								else:
									_cont_int_loc[direccion_dest+(_offsets[0] if _enable_offsets else 0)].valor = int(valores1[0]) * int(valores2[0])
							else:
								# Error: el valor tiene que ser entero 
						else:
							# Error
					elif in_range(direccion_dest, 1000, 2000):
						direccion_dest -= 1000
						if valores1[1] == "Integer" or valores1[1] == "Float" or valores1[1] == "Double":
							if valores2[1] == "Integer" or valores2[1] == "Float" or valores2[1] == "Double":
								if _use_before_offsets_values:
									_cont_flo_loc[direccion_dest+(_before[1] if _enable_offsets else 0)].valor = float(valores1[0]) * float(valores2[0])
								else:
									_cont_flo_loc[direccion_dest+(_offsets[1] if _enable_offsets else 0)].valor = float(valores1[0]) * float(valores2[0])
							else:
								# Error
						else:
							# Error
					elif in_range(direccion_dest, 2000, 3000):
						direccion_dest -= 2000
						if valores1[1] == "Integer" or valores1[1] == "Float" or valores1[1] == "Double":
							if valores2[1] == "Integer" or valores2[1] == "Float" or valores2[1] == "Double":
								if _use_before_offsets_values:
									_cont_dou_loc[direccion_dest+(_before[2] if _enable_offsets else 0)].valor = float(valores1[0]) * float(valores2[0])
								else:
									_cont_dou_loc[direccion_dest+(_offsets[2] if _enable_offsets else 0)].valor = float(valores1[0]) * float(valores2[0])
							else:
								# Error
						else:
							# Error
					elif in_range(direccion_dest, 3000, 4000):
						direccion_dest -= 3000
					elif in_range(direccion_dest, 4000, 5000):
						direccion_dest -= 4000
					elif in_range(direccion_dest, 5000, 6000):
						direccion_dest -= 5000
					elif in_range(direccion_dest, 6000, 7000):
						direccion_dest -= 6000
				elif in_range(direccion_dest, 14000, 21000):
					direccion_dest -= 14000
					if in_range(direccion_dest, 0, 1000):
						if valores1[1] == "Integer" or valores1[1] == "Float" or valores1[1] == "Double":
							if valores2[1] == "Integer" or valores2[1] == "Float" or valores2[1] == "Double":
								if _use_before_offsets_values:
									_cont_int_tmp[direccion_dest+(_before[7] if _enable_offsets else 0)].valor = int(valores1[0]) * int(valores2[0])
								else:
									_cont_int_tmp[direccion_dest+(_offsets[7] if _enable_offsets else 0)].valor = int(valores1[0]) * int(valores2[0])
							else:
								# Error: el valor tiene que ser entero 
						else:
							# Error
					elif in_range(direccion_dest, 1000, 2000):
						direccion_dest -= 1000
						if valores1[1] == "Integer" or valores1[1] == "Float" or valores1[1] == "Double":
							if valores2[1] == "Integer" or valores2[1] == "Float" or valores2[1] == "Double":
								if _use_before_offsets_values:
									_cont_flo_tmp[direccion_dest+(_before[8] if _enable_offsets else 0)].valor = float(valores1[0]) * float(valores2[0])
								else:
									_cont_flo_tmp[direccion_dest+(_offsets[8] if _enable_offsets else 0)].valor = float(valores1[0]) * float(valores2[0])
							else:
								# Error
						else:
							# Error
					elif in_range(direccion_dest, 2000, 3000):
						direccion_dest -= 2000
						if valores1[1] == "Integer" or valores1[1] == "Float" or valores1[1] == "Double":
							if valores2[1] == "Integer" or valores2[1] == "Float" or valores2[1] == "Double":
								if _use_before_offsets_values:
									_cont_dou_tmp[direccion_dest+(_before[9] if _enable_offsets else 0)].valor = float(valores1[0]) * float(valores2[0])
								else:
									_cont_dou_tmp[direccion_dest+(_offsets[9] if _enable_offsets else 0)].valor = float(valores1[0]) * float(valores2[0])
							else:
								# Error
						else:
							# Error
					elif in_range(direccion_dest, 3000, 4000):
						direccion_dest -= 3000
					elif in_range(direccion_dest, 4000, 5000):
						direccion_dest -= 4000
					elif in_range(direccion_dest, 5000, 6000):
						direccion_dest -= 5000
					elif in_range(direccion_dest, 6000, 7000):
						direccion_dest -= 6000
				else:
					direccion_dest -= 21000
					if in_range(direccion_dest, 0, 1000):
						if valores1[1] == "Integer" or valores1[1] == "Float" or valores1[1] == "Double":
							if valores2[1] == "Integer" or valores2[1] == "Float" or valores2[1] == "Double":
								_cont_int_cons[direccion_dest].valor = int(valores1[0]) * int(valores2[0])
							else:
								# Error: el valor tiene que ser entero 															
						else:
							# Error
					elif in_range(direccion_dest, 1000, 2000):
						direccion_dest -= 1000
						if valores1[1] == "Integer" or valores1[1] == "Float" or valores1[1] == "Double":
							if valores2[1] == "Integer" or valores2[1] == "Float" or valores2[1] == "Double":
								_cont_flo_cons[direccion_dest].valor = float(valores1[0]) * float(valores2[0])
							else:
								# Error
						else:
							# Error
					elif in_range(direccion_dest, 2000, 3000):
						direccion_dest -= 2000
						if valores1[1] == "Integer" or valores1[1] == "Float" or valores1[1] == "Double":
							if valores2[1] == "Integer" or valores2[1] == "Float" or valores2[1] == "Double":
								_cont_dou_cons[direccion_dest].valor = float(valores1[0]) * float(valores2[0])
							else:
								# Error
						else:
							# Error
					elif in_range(direccion_dest, 3000, 4000):
						direccion_dest -= 3000
					elif in_range(direccion_dest, 4000, 5000):
						direccion_dest -= 4000
					elif in_range(direccion_dest, 5000, 6000):
						direccion_dest -= 5000
					elif in_range(direccion_dest, 6000, 7000):
						direccion_dest -= 6000
			if comando == "/":
				if in_range(direccion_dest, 0, 7000):
					if in_range(direccion_dest, 0, 1000):
						if valores1[1] == "Integer" or valores1[1] == "Float" or valores1[1] == "Double":
							if valores2[1] == "Integer" or valores2[1] == "Float" or valores2[1] == "Double":
								if valores2[0] != 0:
									_cont_int_glo[direccion_dest].valor = int(valores1[0]) / int(valores2[0])
								else:
									print "Error: Sorry! Can't divide by zero."
							else:
								# Error: el valor tiene que ser entero 															
						else:
							# Error
					elif in_range(direccion_dest, 1000, 2000):
						direccion_dest -= 1000
						if valores1[1] == "Integer" or valores1[1] == "Float" or valores1[1] == "Double":
							if valores2[1] == "Integer" or valores2[1] == "Float" or valores2[1] == "Double":
								if valores2[0] != 0:
									_cont_flo_glo[direccion_dest].valor = float(valores1[0]) / float(valores2[0])
								else:
									print "Error: Sorry! Can't divide by zero."
							else:
								# Error
						else:
							# Error
					elif in_range(direccion_dest, 2000, 3000):
						direccion_dest -= 2000
						if valores1[1] == "Integer" or valores1[1] == "Float" or valores1[1] == "Double":
							if valores2[1] == "Integer" or valores2[1] == "Float" or valores2[1] == "Double":
								if valores2[0] != 0:
									_cont_dou_glo[direccion_dest].valor = float(valores1[0]) / float(valores2[0])
								else:
									print "Error: Sorry! Can't divide by zero."
							else:
								# Error
						else:
							# Error
					elif in_range(direccion_dest, 3000, 4000):
						direccion_dest -= 3000
					elif in_range(direccion_dest, 4000, 5000):
						direccion_dest -= 4000
					elif in_range(direccion_dest, 5000, 6000):
						direccion_dest -= 5000
					elif in_range(direccion_dest, 6000, 7000):
						direccion_dest -= 6000
				elif in_range(direccion_dest, 7000, 14000):
					direccion_dest -= 7000
					if in_range(direccion_dest, 0, 1000):
						if valores1[1] == "Integer" or valores1[1] == "Float" or valores1[1] == "Double":
							if valores2[1] == "Integer" or valores2[1] == "Float" or valores2[1] == "Double":
								if valores2[0] != 0:
									if _use_before_offsets_values:
										_cont_int_loc[direccion_dest+(_before[0] if _enable_offsets else 0)].valor = int(valores1[0]) / int(valores2[0])
									else:
										_cont_int_loc[direccion_dest+(_offsets[0] if _enable_offsets else 0)].valor = int(valores1[0]) / int(valores2[0])
								else:
									print "Error: Sorry! Can't divide by zero."
							else:
								# Error: el valor tiene que ser entero 
						else:
							# Error
					elif in_range(direccion_dest, 1000, 2000):
						direccion_dest -= 1000
						if valores1[1] == "Integer" or valores1[1] == "Float" or valores1[1] == "Double":
							if valores2[1] == "Integer" or valores2[1] == "Float" or valores2[1] == "Double":
								if valores2[0] != 0:
									if _use_before_offsets_values:
										_cont_flo_loc[direccion_dest+(_before[1] if _enable_offsets else 0)].valor = float(valores1[0]) / float(valores2[0])
									else:
										_cont_flo_loc[direccion_dest+(_offsets[1] if _enable_offsets else 0)].valor = float(valores1[0]) / float(valores2[0])
								else:
									print "Error: Sorry! Can't divide by zero."
							else:
								# Error
						else:
							# Error
					elif in_range(direccion_dest, 2000, 3000):
						direccion_dest -= 2000
						if valores1[1] == "Integer" or valores1[1] == "Float" or valores1[1] == "Double":
							if valores2[1] == "Integer" or valores2[1] == "Float" or valores2[1] == "Double":
								if valores2[0] != 0:
									if _use_before_offsets_values:
										_cont_dou_loc[direccion_dest+(_before[2] if _enable_offsets else 0)].valor = float(valores1[0]) / float(valores2[0])
									else:
										_cont_dou_loc[direccion_dest+(_offsets[2] if _enable_offsets else 0)].valor = float(valores1[0]) / float(valores2[0])
								else:
									print "Error: Sorry! Can't divide by zero."
							else:
								# Error
						else:
							# Error
					elif in_range(direccion_dest, 3000, 4000):
						direccion_dest -= 3000
					elif in_range(direccion_dest, 4000, 5000):
						direccion_dest -= 4000
					elif in_range(direccion_dest, 5000, 6000):
						direccion_dest -= 5000
					elif in_range(direccion_dest, 6000, 7000):
						direccion_dest -= 6000
				elif in_range(direccion_dest, 14000, 21000):
					direccion_dest -= 14000
					if in_range(direccion_dest, 0, 1000):
						if valores1[1] == "Integer" or valores1[1] == "Float" or valores1[1] == "Double":
							if valores2[1] == "Integer" or valores2[1] == "Float" or valores2[1] == "Double":
								if valores2[0] != 0:
									if _use_before_offsets_values:
										_cont_int_tmp[direccion_dest+(_before[0] if _enable_offsets else 0)].valor = int(valores1[0]) / int(valores2[0])
									else:
										_cont_int_tmp[direccion_dest+(_offsets[0] if _enable_offsets else 0)].valor = int(valores1[0]) / int(valores2[0])
								else:
									print "Error: Sorry! Can't divide by zero."
							else:
								# Error: el valor tiene que ser entero 
						else:
							# Error
					elif in_range(direccion_dest, 1000, 2000):
						direccion_dest -= 1000
						if valores1[1] == "Integer" or valores1[1] == "Float" or valores1[1] == "Double":
							if valores2[1] == "Integer" or valores2[1] == "Float" or valores2[1] == "Double":
								if valores2[0] != 0:
									if _use_before_offsets_values:
										_cont_flo_tmp[direccion_dest+(_before[1] if _enable_offsets else 0)].valor = float(valores1[0]) / float(valores2[0])
									else:
										_cont_flo_tmp[direccion_dest+(_offsets[1] if _enable_offsets else 0)].valor = float(valores1[0]) / float(valores2[0])
								else:
									print "Error: Sorry! Can't divide by zero."
							else:
								# Error
						else:
							# Error
					elif in_range(direccion_dest, 2000, 3000):
						direccion_dest -= 2000
						if valores1[1] == "Integer" or valores1[1] == "Float" or valores1[1] == "Double":
							if valores2[1] == "Integer" or valores2[1] == "Float" or valores2[1] == "Double":
								if valores2[0] != 0:
									if _use_before_offsets_values:
										_cont_dou_tmp[direccion_dest+(_before[2] if _enable_offsets else 0)].valor = float(valores1[0]) / float(valores2[0])
									else:
										_cont_dou_tmp[direccion_dest+(_offsets[2] if _enable_offsets else 0)].valor = float(valores1[0]) / float(valores2[0])
								else:
									print "Error: Sorry! Can't divide by zero."
							else:
								# Error
						else:
							# Error
					elif in_range(direccion_dest, 3000, 4000):
						direccion_dest -= 3000
					elif in_range(direccion_dest, 4000, 5000):
						direccion_dest -= 4000
					elif in_range(direccion_dest, 5000, 6000):
						direccion_dest -= 5000
					elif in_range(direccion_dest, 6000, 7000):
						direccion_dest -= 6000
				else:
					direccion_dest -= 21000
					if in_range(direccion_dest, 0, 1000):
						if valores1[1] == "Integer" or valores1[1] == "Float" or valores1[1] == "Double":
							if valores2[1] == "Integer" or valores2[1] == "Float" or valores2[1] == "Double":
								if valores2[0] != 0:
									_cont_int_cons[direccion_dest].valor = int(valores1[0]) / int(valores2[0])
								else:
									print "Error: Sorry! Can't divide by zero."
							else:
								# Error: el valor tiene que ser entero 															
						else:
							# Error
					elif in_range(direccion_dest, 1000, 2000):
						direccion_dest -= 1000
						if valores1[1] == "Integer" or valores1[1] == "Float" or valores1[1] == "Double":
							if valores2[1] == "Integer" or valores2[1] == "Float" or valores2[1] == "Double":
								if valores2[0] != 0:
									_cont_flo_cons[direccion_dest].valor = float(valores1[0]) / float(valores2[0])
								else:
									print "Error: Sorry! Can't divide by zero."
							else:
								# Error
						else:
							# Error
					elif in_range(direccion_dest, 2000, 3000):
						direccion_dest -= 2000
						if valores1[1] == "Integer" or valores1[1] == "Float" or valores1[1] == "Double":
							if valores2[1] == "Integer" or valores2[1] == "Float" or valores2[1] == "Double":
								if valores2[0] != 0:
									_cont_dou_cons[direccion_dest].valor = float(valores1[0]) / float(valores2[0])
								else:
									print "Error: Sorry! Can't divide by zero."
							else:
								# Error
						else:
							# Error
					elif in_range(direccion_dest, 3000, 4000):
						direccion_dest -= 3000
					elif in_range(direccion_dest, 4000, 5000):
						direccion_dest -= 4000
					elif in_range(direccion_dest, 5000, 6000):
						direccion_dest -= 5000
					elif in_range(direccion_dest, 6000, 7000):
						direccion_dest -= 6000


	# Devuelve el valor de la direccion que se proporciona y regresa valor y tipo de dato
	def get_valor(self, direccion_var, offsets):
		valores = [""] * 2
		if direccion_var >= 0 and direccion_var < 7000:
			if direccion_var >= 0 and direccion_var < 1000:
				valores[0] = str(_cont_int_glo[direccion_var].valor)
				valores[1] = _cont_int_glo[direccion_var].dataType
			elif direccion_var >= 1000 and direccion_var < 2000:
				direccion_var -= 1000
				valores[0] = str(_cont_flo_glo[direccion_var].valor)
				valores[1] = _cont_flo_glo[direccion_var].dataType
			elif direccion_var >= 2000 and direccion_var < 3000:
				direccion_var -= 2000
				valores[0] = str(_cont_dou_glo[direccion_var].valor)
				valores[1] = _cont_dou_glo[direccion_var].dataType
			elif direccion_var >= 3000 and direccion_var < 4000:
				direccion_var -= 3000
				valores[0] = str(_cont_str_glo[direccion_var].valor)
				valores[1] = _cont_str_glo[direccion_var].dataType
			elif direccion_var >= 4000 and direccion_var < 5000:
				direccion_var -= 5000
				valores[0] = str(_cont_bool_glo[direccion_var].valor)
				valores[1] = _cont_bool_glo[direccion_var].dataType
			elif direccion_var >= 5000 and direccion_var < 6000:
				direccion_var -= 5000
				valores[0] = str(_cont_list_glo[direccion_var].valor)
				valores[1] = _cont_list_glo[direccion_var].dataType
			elif direccion_var >= 6000 and direccion_var < 7000:
				direccion_var -= 6000
				valores[0] = str(_cont_arr_glo[direccion_var].valor)
				valores[1] = _cont_arr_glo[direccion_var].dataType
			else:
				direccion_var -= 7000 # Revisar
		elif direccion_var >= 7000 and direccion_var < 14000:
			direccion_var -= 7000
			if direccion_var >= 0 and direccion_var < 1000:
				valores[0] = str(_cont_int_loc[direccion_var+(offsets[0] if _enable_offsets else 0)].valor)
				valores[1] = _cont_int_loc[direccion_var+(offsets[0] if _enable_offsets else 0)].dataType
			elif direccion_var >= 1000 and direccion_var < 2000:
				direccion_var -= 1000
				valores[0] = str(_cont_flo_loc[direccion_var+(offsets[1] if _enable_offsets else 0)].valor)
				valores[1] = _cont_flo_loc[direccion_var+(offsets[1] if _enable_offsets else 0)].dataType
			elif direccion_var >= 2000 and direccion_var < 3000:
				direccion_var -= 2000
				valores[0] = str(_cont_dou_loc[direccion_var+(offsets[2] if _enable_offsets else 0)].valor)
				valores[1] = _cont_dou_loc[direccion_var+(offsets[2] if _enable_offsets else 0)].dataType
			elif direccion_var >= 3000 and direccion_var < 4000:
				direccion_var -= 3000
				valores[0] = str(_cont_str_loc[direccion_var+(offsets[3] if _enable_offsets else 0)].valor)
				valores[1] = _cont_str_loc[direccion_var+(offsets[3] if _enable_offsets else 0)].dataType
			elif direccion_var >= 4000 and direccion_var < 5000:
				direccion_var -= 4000
				valores[0] = str(_cont_bool_loc[direccion_var+(offsets[4] if _enable_offsets else 0)].valor)
				valores[1] = _cont_bool_loc[direccion_var+(offsets[4] if _enable_offsets else 0)].dataType
			elif direccion_var >= 5000 and direccion_var < 6000:
				direccion_var -= 5000
				valores[0] = str(_cont_list_loc[direccion_var+(offsets[5] if _enable_offsets else 0)].valor)
				valores[1] = _cont_list_loc[direccion_var+(offsets[5] if _enable_offsets else 0)].dataType
			elif direccion_var >= 6000 and direccion_var < 7000:
				direccion_var -= 6000
				valores[0] = str(_cont_arr_loc[direccion_var+(offsets[6] if _enable_offsets else 0)].valor)
				valores[1] = _cont_arr_loc[direccion_var+(offsets[6] if _enable_offsets else 0)].dataType
			else:
				direccion_var -= 7000 # Revisar
		elif direccion_var >= 14000 and direccion_var < 21000:
			direccion_var -= 14000
			if direccion_var >= 0 and direccion_var < 1000:
				valores[0] = str(_cont_int_tmp[direccion_var+(offsets[7] if _enable_offsets else 0)].valor)
				valores[1] = _cont_int_tmp[direccion_var+(offsets[7] if _enable_offsets else 0)].dataType
			elif direccion_var >= 1000 and direccion_var < 2000:
				direccion_var -= 1000
				valores[0] = str(_cont_flo_tmp[direccion_var+(offsets[8] if _enable_offsets else 0)].valor)
				valores[1] = _cont_flo_tmp[direccion_var+(offsets[8] if _enable_offsets else 0)].dataType
			elif direccion_var >= 2000 and direccion_var < 3000:
				direccion_var -= 2000
				valores[0] = str(_cont_dou_tmp[direccion_var+(offsets[9] if _enable_offsets else 0)].valor)
				valores[1] = _cont_dou_tmp[direccion_var+(offsets[9] if _enable_offsets else 0)].dataType
			elif direccion_var >= 3000 and direccion_var < 4000:
				direccion_var -= 3000
				valores[0] = str(_cont_str_tmp[direccion_var+(offsets[10] if _enable_offsets else 0)].valor)
				valores[1] = _cont_str_tmp[direccion_var+(offsets[10] if _enable_offsets else 0)].dataType
			elif direccion_var >= 4000 and direccion_var < 5000:
				direccion_var -= 4000
				valores[0] = str(_cont_bool_tmp[direccion_var+(offsets[11] if _enable_offsets else 0)].valor)
				valores[1] = _cont_bool_tmp[direccion_var+(offsets[11] if _enable_offsets else 0)].dataType
			elif direccion_var >= 5000 and direccion_var < 6000:
				direccion_var -= 5000
				valores[0] = str(_cont_list_tmp[direccion_var+(offsets[12] if _enable_offsets else 0)].valor)
				valores[1] = _cont_list_tmp[direccion_var+(offsets[12] if _enable_offsets else 0)].dataType
			elif direccion_var >= 6000 and direccion_var < 7000:
				direccion_var -= 6000
				valores[0] = str(_cont_arr_tmp[direccion_var+(offsets[13] if _enable_offsets else 0)].valor)
				valores[1] = _cont_arr_tmp[direccion_var+(offsets[13] if _enable_offsets else 0)].dataType
			else:
				direccion_var -= 7000 # Revisar
		else:
			direccion_var -= 21000
			if direccion_var >= 0 and direccion_var < 1000:
				valores[0] = str(_cont_int_cons[direccion_var].valor)
				valores[1] = _cont_int_cons[direccion_var].dataType
			elif direccion_var >= 1000 and direccion_var < 2000:
				direccion_var -= 1000
				valores[0] = str(_cont_flo_cons[direccion_var].valor)
				valores[1] = _cont_flo_cons[direccion_var].dataType
			elif direccion_var >= 2000 and direccion_var < 3000:
				direccion_var -= 2000
				valores[0] = str(_cont_dou_cons[direccion_var].valor)
				valores[1] = _cont_dou_cons[direccion_var].dataType
			elif direccion_var >= 3000 and direccion_var < 4000:
				direccion_var -= 3000
				valores[0] = str(_cont_str_cons[direccion_var].valor)
				valores[1] = _cont_str_cons[direccion_var].dataType
			elif direccion_var >= 4000 and direccion_var < 5000:
				direccion_var -= 4000
				valores[0] = str(_cont_bool_cons[direccion_var].valor)
				valores[1] = _cont_bool_cons[direccion_var].dataType
			elif direccion_var >= 5000 and direccion_var < 6000:
				direccion_var -= 5000
				valores[0] = str(_cont_list_cons[direccion_var].valor)
				valores[1] = _cont_list_cons[direccion_var].dataType
			elif direccion_var >= 6000 and direccion_var < 7000:
				direccion_var -= 6000
				valores[0] = str(_cont_arr_cons[direccion_var].valor)
				valores[1] = _cont_arr_cons[direccion_var].dataType
			else:
				direccion_var -= 7000 # Revisar

		return valores

	# Carga las variables locales y temporales de una funcion
	def carga_proc(self, nombre):
		proc_a_cargar = 0

		while _procedimientos[proc_a_cargar]._nombre != nombre:
			proc_a_cargar += 1

		_cont_int_loc = [VariableInt()] * _procedimientos[proc_a_cargar]._vars_int_loc
		_cont_flo_loc = [VariableFloat()] * _procedimientos[proc_a_cargar]._vars_flo_loc
		_cont_dou_loc = [VariableDouble()] * _procedimientos[proc_a_cargar]._vars_dou_loc
		_cont_str_loc = [VariableStr()] * _procedimientos[proc_a_cargar]._vars_str_loc
		_cont_bool_loc = [VariableBool()] * _procedimientos[proc_a_cargar]._vars_bool_loc
		_cont_list_loc = [VariableList()] * _procedimientos[proc_a_cargar]._vars_list_loc
		_cont_arr_loc = [VariableArray()] * _procedimientos[proc_a_cargar]._vars_arr_loc

		_cont_int_tmp = [VariableInt()] * _procedimientos[proc_a_cargar]._vars_int_tmp
		_cont_flo_tmp = [VariableFloat()] * _procedimientos[proc_a_cargar]._vars_flo_tmp
		_cont_dou_tmp = [VariableDouble()] * _procedimientos[proc_a_cargar]._vars_dou_tmp
		_cont_str_tmp = [VariableStr()] * _procedimientos[proc_a_cargar]._vars_str_tmp
		_cont_bool_tmp = [VariableBool()] * _procedimientos[proc_a_cargar]._vars_bool_tmp
		_cont_list_tmp = [VariableList()] * _procedimientos[proc_a_cargar]._vars_list_tmp
		_cont_arr_tmp = [VariableArray()] * _procedimientos[proc_a_cargar]._vars_arr_tmp

	def descarga_proc(self, nombre):
		pass

	# Devuelve el cuadruplo inicial de la funcion
	def get_num_ins(self, nombre):
		proc_a_cargar = 0

		while _procedimientos[proc_a_cargar]._nombre != nombre:
			proc_a_cargar += 1

		return _procedimientos[proc_a_cargar]._cuadruplo_inicio

	def clear_all(self):
		# Globales
		del _cont_int_glo[:]
		del _cont_flo_glo[:]
		del _cont_dou_glo[:]
		del _cont_str_glo[:]
		del _cont_bool_glo[:]
		del _cont_list_glo[:]
		del _cont_arr_glo[:]

		# Locales
		del _cont_int_loc[:]
		del _cont_flo_loc[:]
		del _cont_dou_loc[:]
		del _cont_str_loc[:]
		del _cont_bool_loc[:]
		del _cont_list_loc[:]
		del _cont_arr_loc[:]

		# Temporales
		del _cont_int_tmp[:]
		del _cont_flo_tmp[:]
		del _cont_dou_tmp[:]
		del _cont_str_tmp[:]
		del _cont_bool_tmp[:]
		del _cont_list_tmp[:]
		del _cont_arr_tmp[:]

		# Constantes
		del _cont_int_cons[:]
		del _cont_flo_cons[:]
		del _cont_dou_cons[:]
		del _cont_str_cons[:]
		del _cont_bool_cons[:]
		del _cont_list_cons[:]
		del _cont_arr_cons[:]

		del cuadruplos[:]
		del _procedimientos[:]

		_apuntador = 0

		_apuntador_inst = [0] * 1000

		_offsets = [0] * 8

	# Funciones adicionales
	# Devuelve True si la direcccion (direc) se encuentra dentro del rango ini fin; devuelve False en cualquier otro caso
	def in_range(direc, ini, fin):
		if direc >= ini and direc < fin:
			return True
		else:
			return False

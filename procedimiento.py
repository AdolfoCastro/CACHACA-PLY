class Procedimiento():
  _nombre = ""
	_cuadruplo_inicio = 0

	_vars_int_loc = 0
	_vars_flo_loc = 0
	_vars_dou_loc = 0
	_vars_str_loc = 0
	_vars_bool_loc = 0
	_vars_list_loc = 0
	_vars_arr_loc = 0

	_vars_int_tmp = 0
	_vars_flo_tmp = 0
	_vars_dou_tmp = 0
	_vars_str_tmp = 0
	_vars_bool_tmp = 0
	_vars_list_tmp = 0
	_vars_arr_tmp = 0

	__init__(nombre, cuadruplo_inicio, vars_int_loc, vars_flo_loc, vars_dou_loc, vars_str_loc, 
		vars_bool_loc, vars_list_loc, vars_arr_loc, vars_int_tmp, vars_flo_tmp, vars_dou_tmp,
		vars_str_tmp, vars_bool_tmp, vars_list_tmp, vars_arr_tmp):

		self._nombre = nombre
		self._cuadruplo_inicio = cuadruplo_inicio

		self._vars_int_loc = vars_int_loc
		self._vars_flo_loc = vars_flo_loc
		self._vars_dou_loc = vars_dou_loc
		self._vars_str_loc = vars_str_loc
		self._vars_bool_loc = vars_bool_loc
		self._vars_list_loc = vars_list_loc
		self._vars_arr_loc = vars_arr_loc

		self._vars_int_tmp = vars_int_tmp
		self._vars_flo_tmp = vars_flo_tmp
		self._vars_dou_tmp = vars_dou_tmp
		self._vars_str_tmp = vars_str_tmp
		self._vars_bool_tmp = vars_bool_tmp
		self._vars_list_tmp = vars_list_tmp
		self._vars_arr_tmp = vars_arr_tmp

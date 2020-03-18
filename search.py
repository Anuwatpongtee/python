if request.method == "GET":
    if 'search_btn' in request.form:
        todo = ref.order_by_child('detail').start_at("ข้อมูลที่ต้องการค้นหา\uf8ff").end_at("\uf8ff").get()

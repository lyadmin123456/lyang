<template>
  <div id="wrap">
    <div id="top_content">
      <div id="header">
        <div id="rightheader">
          <p>
            2020/09/20
            <br />
          </p>
        </div>
        <div id="topheader">
          <h1 id="title">
            <a href="#">Main</a>
          </h1>
        </div>
        <div id="navigation">
        </div>
      </div>
      <div id="content">
        <p id="whereami">
        </p>
        <h1>
         update Emp info:{{$route.params.id}}
        </h1>
        <form action="emp_list.html" method="post">
          <table cellpadding="0" cellspacing="0" border="0"
                 class="form_table">
            <tr>
              <td valign="middle" align="right">
                id:
              </td>
              <td valign="middle" align="left">
                {{emp_id}}
              </td>
            </tr>
            <tr>
              <td valign="middle" align="right">
                name:
              </td>
              <td valign="middle" align="left">
                <input type="text" class="inputgri" name="name" v-model="up_name"/>
              </td>
            </tr>
            <tr>
              <td valign="middle" align="right">
                photo:
              </td>
              <td valign="middle" align="left">
                <img src="ems.img" alt="" width="60" height="60" >
                <input type="file" name="photo" ref="img"/>
              </td>
            </tr>
            <tr>
              <td valign="middle" align="right">
                salary:
              </td>
              <td valign="middle" align="left">
                <input type="text" class="inputgri" name="salary" v-model="up_salary"/>
              </td>
            </tr>
            <tr>
              <td valign="middle" align="right">
                age:
              </td>
              <td valign="middle" align="left">
                <input type="text" class="inputgri" name="age" v-model="up_age"/>
              </td>
            </tr>
          </table>
          <p>
           <input type="button" class="button" value="提交" @click="click" />
          </p>
        </form>
      </div>
    </div>
    <div id="footer">
      <div id="footer_bg">
        ABC@126.com
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "Update",
  data(){
    return{
      up_id:'',
      up_name:'',
      up_salary:'',
      up_age:'',
      up_img:'',
    }
  },
  methods:{
    Get_Up(){
      let up_id=this.$route.params.id
      this.$axios.get('http://127.0.0.1:8000/api/emps/'+`${up_id}`).then(res=>{
        this.up_id=res.data.result['id']
        this.up_name=res.data.result['up_name']
        this.up_salary=res.data.result['salary']
        this.up_age=res.data.result['age']
        this.up_img=res.data.result['img']
      }).catch(error=>{
        this.$message('用户信息不存在');
      })
    },
    click() {
      let formData = new FormData();
      formData.append("name", this.up_name);
      formData.append("img", this.$refs.img.files[0]);
      formData.append("salary", this.up_salary);
      formData.append("age", this.up_age);
      this.$axios({
        url: "http://127.0.0.1:8000/api/emps/"+`${this.up_id}`,
        method: "patch",
        data: formData,
        headers:{
          'content-type': 'multipart/form-data',
        },
      }).then(res => {
        console.log(res.data.result)
        this.$message('已修改');
        this.$router.push('/index')
      }).catch(error => {
        this.$message.error("修改失败")
      })
    }
  },
  created() {
    this.Get_Up()
  }
}



</script>

<style scoped>

</style>

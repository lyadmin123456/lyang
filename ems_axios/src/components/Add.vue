<template>
  <div id="wrap">
    <div id="top_content">
      <div id="header">
        <div id="rightheader">
          <p>
            2020/09/17
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
          添加员工
        </h1>
        <table cellpadding="0" cellspacing="0" border="0"
               class="form_table">
          <tr>
            <td valign="middle" align="right">
              name:
            </td>
            <td valign="middle" align="left">
              <input type="text" class="inputgri" name="name" v-model="emp_name"/>
            </td>
          </tr>
          <tr>
            <td valign="middle" align="right">
              photo:
            </td>
            <td valign="middle" align="left">
              <input type="file" name="photo" ref="img"/>
            </td>
          </tr>
          <tr>
            <td valign="middle" align="right">
              salary:
            </td>
            <td valign="middle" align="left">
              <input type="text" class="inputgri" name="salary" v-model="salary"/>
            </td>
          </tr>
          <tr>
            <td valign="middle" align="right">
              age:
            </td>
            <td valign="middle" align="left">
              <input type="text" class="inputgri" name="age" v-model="age"/>
            </td>
          </tr>
        </table>
        <p>
<!--           <input type="添加员工" class="button" value="添加员工" @click="add_emp"/>-->
          <el-button type="primary"  @click="add_emp">添加员工</el-button>
        </p>
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
  name: "Add",
  data(){
    return{
      emp_name:'',
      age:'',
      salary:'',
      img:'',
    }
  },
  methods:{
    add_emp(){
    //  获取文件信息
      let file=this.$refs.img.files[0]

    //  发送axios请求
      let formData=new FormData();
      formData.append('emp_name',this.emp_name);
      formData.append('salary',this.salary);
      formData.append('age',this.age);
      formData.append('img',this.file);
     this.$axios({
       url:'http://127.0.0.1:8000/api/emps/',
       method:'post',
       data:formData,
       headers:{
         "content-type": "multipart/form-data"
       },
     }).then(response=>{
       console.log(response.data);
       if (response.data.message){
         this.$message({
           message:'添加成功',
           type:'success',
           duration:1000,
           showClose:true,
         })
       //  跳转员工列表
         this.$router.push('/index');
       }
     }).catch(error=>{
       console.log(error.message);
     })
    }
  },
  created(){
    let mes=localStorage.getItem('users')
    if (mes){

    }else{
      this.$message.error('请登录')
      this.$router.push('/Login')
    }
  }
}
</script>

<style scoped>

</style>

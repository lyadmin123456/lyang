<template>
  <div id="wrap">
    <div id="top_content">
      <div id="header">
        <div id="rightheader">
          <p>
            2009/11/20
            <br />
            安全退出
          </p>
        </div>
        <div id="topheader">
          <h1 id="title">
            <a href="#">main</a>
          </h1>
        </div>
        <div id="navigation">
        </div>
      </div>
      <div id="content">
        <p id="whereami">
        </p>
        <h1>
           Welcome:{{user}}
        </h1>
        <table class="table">
          <tr class="table_header">
            <td>ID</td>
            <td>Name</td>
            <td>Photo</td>
            <td>Salary</td>
            <td>Age</td>
            <td>Operation</td>
          </tr>
          <tr class="row1" v-for="(emp,index) in emp_list" :key="emp.id :class="index%2==0?'row1':'row2'">
            <td>{{emp.id}}</td>
            <td>{{emp.emp_name}}</td>
            <td><img src="ems.img" style="height: 60px;"></td>
            <td>{{emp.salary}}</td>
            <td>{{emp.age}}</td>
            <td>
              <a href="javascript:;" @click="del_emp(emp.id)">删除</a>&nbsp;
              <router-link :to="'/update/'+emp.id">修改</router-link>
                          </td>
                        </tr>

                      </table>
                      <p>
                        <!--                    <input type="button" class="el-button" value="添加员工"/>-->
          <el-button plain>
            <router-link to="/add">
               添加员工
            </router-link>
          </el-button>
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
  name: "index",
  data(){
    return{
      user_msg:'',
      emp_list:[],
    }
  },
  methods:{
  //  获取所有信息
    getAllEmp(){
      this.$axios.get('http://127.0.0.1:8000/api/emps/').then(response=>{
        this.emp_list=response.data.results;
      }).catch(error=>{
          this.$message.error('查询有误')
      })
    },
  //  删除员工
    del_emp(id){
    //  根据id删除
      this.$axios({
        url:'http://127.0.0.1:8000/api/emps/'+`${id}`,
        method:'del',
      }).then(response=>{
        this.$message('已删除');

      }).catch(error=>{
        this.$message.error('删除失败');
      })
      console.log(index);
      this.emp_list.splice(index,1)
    },
//生命周期钩子函数
  created() {
    let username=sessionStorage.getItem('user');
    if (username){
      this.user_msg=username;
    }else {
      this.$message.error('请返回登录');
      this.$router.push('/Login');
    }
    this.getAllEmp();
  }
 }
}


</script>

<style scoped>

</style>

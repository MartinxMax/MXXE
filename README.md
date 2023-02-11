 <div align="center">
 <img src="https://readme-typing-svg.herokuapp.com/?lines=This+is+a+XXE+vulnerability+exploitation+tool.;---@Мартин.&font=Roboto" />
 <p align="center">
 <img title="MXXE" src='https://img.shields.io/badge/MXXE-1.0.0-brightgreen.svg' />
 <img title="MXXE" src='https://img.shields.io/badge/XXE-Tool'/>
 <img title="MXXE" src='https://img.shields.io/badge/Python-3.9-yellow.svg' />
  <img title="MXXE" src='https://img.shields.io/badge/HackerTool-x' />
 <img title="MXXE" src='https://img.shields.io/static/v1?label=Author&message=@Martin&color=red'/>
 <img title="MXXE" src='https://img.shields.io/badge/-Linux-F16061?logo=linux&logoColor=000'/>
 </p>
  <img height="137px" src="https://github-readme-stats.vercel.app/api?username=MartinXMax&hide_title=true&hide_border=true&show_icons=trueline_height=21&text_color=000&icon_color=000&bg_color=0,ea6161,ffc64d,fffc4d,52fa5a&theme=graywhite" />
 <table>
  <tr>
      <th>Function</th>
  </tr>
  <tr>
    <th>XXE vulnerability data receiver</th>
  </tr>
 </table>
</div>

# usage method

```#python3 MXXE.py -h```

 ![图片名称](./Pt/help0.png)  

## practice

1.Port scan

 ![图片名称](./Pt/Scan1.png)

2.Mining to robots file

![图片名称](./Pt/robots2.png)

3.Determine XML format transmission and detect XXE vulnerability

 ![图片名称](./Pt/xxe4.png)
 
4.Run tool(Use TCP tunnel for public network deployment)

 ![图片名称](./Pt/runing3.png)
 
5.The server parses the XML code and determines that there is an XXE entity vulnerability

--We got the file content on the server

 ![图片名称](./Pt/XXE5.png)

6.After decryption, PHP executes to get Flag

 ![图片名称](./Pt/xxe6.png)


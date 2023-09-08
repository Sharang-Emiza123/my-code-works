function numFunc(val) {
    var txt = document.getElementById('txt')
    txt.value += val;
  }
  
  function opFunc(val) {
    var txt = document.getElementById('txt')
    txt.value += val;
  }
  
  function delFunc(){
    var txtval = document.getElementById('txt').value
    txtval = txtval.slice(0,-1)
    document.getElementById('txt').value = txtval
  }

 function eqlFunc(){
  var txtval = document.getElementById('txt').value
  // let pattern = /\W/g;
  let pattern = /[/,+,*,-]/g;
  let result = txtval.match(pattern);

  if (result != null) {
    var valarr = txtval.split(pattern)
    const numarr = []
    for (let i = 0; i < valarr.length; i++) {
      numarr.push(parseInt(valarr[i]))
    }
    console.log(typeof(result));
    console.log(result);
    console.log(valarr);
    console.log(numarr);
    switch (result[0]) {
        case '/':
          var ans = numarr[0] / numarr[1]
          document.getElementById('txt').value += " = " + ans
          break;
        case '*':
          var ans = numarr[0] * numarr[1]
          document.getElementById('txt').value += " = " + ans
          break;
        case '+':
          var ans = numarr[0] + numarr[1]
          document.getElementById('txt').value += " = " + ans
          break;
        case '-':
          var ans = numarr[0] - numarr[1]
          document.getElementById('txt').value += " = " + ans
          break;
        default:
          txtval = document.getElementById('txt').value
          break;
    }
  } else {
    alert('no operator')
    document.getElementById('txt').value = '';
  }
}
  
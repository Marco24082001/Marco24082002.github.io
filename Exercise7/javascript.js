let fileimgs = document.getElementsByClassName("files");
let nameitems = document.getElementsByClassName("nameitems");
let imgs = document.getElementsByClassName("img");
let submits_btn = document.getElementsByClassName("submit");
let categorys = document.getElementsByClassName("listselect");
let container = document.getElementById("container");
let result_1 = document.getElementsByClassName("result-1");
let result_2 = document.getElementsByClassName("result-2");
let btn_choosefile = document.getElementsByClassName("btn-choosefile");
let header = '<tr><th>#</th><th>Item Name</th><th>Category</th><th>image</th><th>Action</th></tr>'
const regPattern = /^[^0-9][^]{0,8}$/i;
let str;

Showdata();
loadEventfilechange();

// button choose file
function choosefilebtn(index) {
    fileimgs[index].click();
}

// add event file change for every fileimg
function loadEventfilechange() {
    for (let i = 0; i < fileimgs.length; i++) {
        fileimgs[i].addEventListener("change", () => {
            const filename = fileimgs[i].files[0];
            if (filename) {
                const reader = new FileReader();
                reader.onload = function () {
                    const result = reader.result;
                    str = result;
                    imgs[i].src = str;
                }
                reader.readAsDataURL(filename);
            }
        })
    }
}


//validate data
function validateName(value, index) {
    if (regPattern.test(value)) {
        return true;
    }
    else {
        result_1[index].innerHTML = 'Name is required';
        return false;
    }
}

function validateSelect(value, index) {
    if (value == 'No selected') {
        result_2[index].innerHTML = 'Catogory is required';
        return false;
    }
    return true;
}

function validateImg(value, index)  {
    console.log(value.src);
    if(value.src == '') return false;
    return true;
}

function validateForm(index) {
    if (validateName(nameitems[index].value, index) && validateSelect(categorys[index].value, index) && validateImg(imgs[index], index)) {
        return true;
    }
    else {
        validateSelect(categorys[index].value, index);
        return false;
    }
    
}
/////////////

// function add event click submit or save
function onclickSubmit(i) {
    if (validateForm(i)) {
        result_1[i].innerHTML = '';
        result_2[i].innerHTML = '';
        let listArray;
        let data = {};
        data.name = nameitems[i].value;
        data.src = imgs[i].src;
        data.select = categorys[i].value;
        let getLocalstore = localStorage.getItem("ListInfo");
        if (getLocalstore == null) {
            listArray = [];
        }
        else {
            listArray = JSON.parse(getLocalstore);
        }
        if (i == 0) {
            listArray.push(data);
        }
        else {
            listArray[i - 1] = data;
            document.getElementsByClassName("btn-edit")[i-1].classList.remove("submit");
            document.getElementsByClassName("listselect")[i].style['pointer-events'] = 'none';
            document.getElementsByClassName("nameitems")[i].style['pointer-events'] = 'none';
        }
        localStorage.setItem("ListInfo", JSON.stringify(listArray));
        Showdata(); 
        loadEventfilechange();
    }
}

// add event submit for btn submit
submits_btn[0].addEventListener("click", function() {
    onclickSubmit(0);
})



function Showdata() {
    let listArray;
    let getLocalstore = localStorage.getItem("ListInfo");
    if (getLocalstore == null) {
        listArray = [];
    } else {
        listArray = JSON.parse(getLocalstore);
    }
    let newtrtag = header;
    listArray.forEach((element, index) => {
        newtrtag += `<tr>
        <td>${index + 1}</td>
        <td>
            <input class="nameitems" type="text" value = "${element.name}">
            <span class="result-1"></span>
        </td>
        <td >
            <select class= "listselect" disabled >
                <option value="No selected">No selected</option>
                <option value="Category 1">Category 1</option>
                <option value="Category 2">Category 2</option>
                <option value="Category 3">Category 3</option>
                <option value="Category 4">Category 4</option>
            </select>
            <span class="result-2"></span>
        </td>  
        <td>
            <input type="button" onclick="choosefilebtn(${index + 1})" class="btn-choosefile" value="Choose file"></input>
            <img class="img" src=${element.src} alt="" accept="image/x-png,image/jpeg">
            <input class="files" type="file" hidden>
        </td>
        <td>
            <input type="button" class="btn-edit" value="Edit" onclick="edit(${index + 1})"></input>
            <input type="button" class="btn-delete" value="Delete" onclick="Delete(${index})"></input>
        </td>    
    </tr>`
    });
    container.innerHTML = newtrtag;
    for (let i = 0; i < listArray.length; i++) {
        document.getElementsByClassName("listselect")[i + 1].value = listArray[i].select;
    }
}

function edit(index) {
    let btn_delete = document.getElementsByClassName("btn-delete")[index - 1];
    let btn_edit = document.getElementsByClassName("btn-edit")[index - 1];
    if (btn_edit.classList.item(0) == "btn-edit" && !btn_edit.classList.item(1)) {
        btn_edit.classList.add("submit");
        btn_delete.classList.add("Cancel");
        btn_delete.value = "Cancel";
        btn_edit.value = "Save";
        document.getElementsByClassName("nameitems")[index].style['pointer-events'] = 'auto';
        document.getElementsByClassName("listselect")[index].disabled = false;
        btn_choosefile[index-1].style.display = "block";
    }
    else {
        onclickSubmit(index);
    }
}

function Delete(index) {
    let btn_delete = document.getElementsByClassName("btn-delete")[index];
    if(btn_delete.classList.item(1))
    {
        Showdata();
    }
    else{  
        let getLocalStorageData = localStorage.getItem("ListInfo");
        listArray = JSON.parse(getLocalStorageData);
        listArray.splice(index, 1);
        localStorage.setItem("ListInfo", JSON.stringify(listArray));
        Showdata()
    }
}



function createSchedObject(object){


    return({
        name: object.name,
        
    })
}

function createSchedArray(array){
    let schedArray = []
    array.forEach(object => {
        schedArray.push(createSchedObject(object))
    })
    return schedArray
}
import React from 'react'
import {Routes} from "react-router-dom"
import {useState, useEffect} from 'react'

export const CatchData = () => {

  type listData = {
    name: string
    value:string
  }

  const [listdata, setListData]= useState <listData[] | null>(null)

  // 從後端catch data進來
    const catchDataUrl = async () =>{
      await fetch("http://127.0.0.1:5000/")
        .then(response => response.json())
        .then(data => {
          let key = Object.keys(data)
          let dataArray : listData [] = []
          for (let i = 0 ; i < key.length ; i++){
            dataArray.push({
              name : key[i],
              value : data[key[i]]
            })
          }
          setListData(dataArray)
        })
      .catch(error => console.log(error))
    }

    useEffect(() => {
      catchDataUrl()
    })
  return (
    <>
      {
        listdata === null ?
          <tr>
            <td className='textcenter'>
              nodata
            </td>
            <td className='textcenter'>
              loading
            </td>
          </tr>
        :

        <h4>{JSON.stringify(listdata)}<br/></h4>
      }
    </>
  )
}

export default CatchData
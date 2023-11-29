package com.example.myfirebaseexample.api

import com.example.myfirebaseexample.api.response.PostResponse
import com.example.myfirebaseexample.api.response.WeaponResponse
import retrofit2.Retrofit
import retrofit2.converter.gson.GsonConverterFactory
import retrofit2.http.Body

class FirebaseApiAdapter {
    private var URL_BASE = "https://artes-marciales-90334-default-rtdb.firebaseio.com/"
    private val firebaseApi = Retrofit.Builder()
        .baseUrl(URL_BASE)
        .addConverterFactory(GsonConverterFactory.create())
        .build()

    fun getWeapons(): MutableMap<String, WeaponResponse>? {
        val call = firebaseApi.create(FirebaseApi::class.java).getWeapons().execute()
        val weapons = call.body()
        return weapons
    }

    fun getWeapon(id: String): WeaponResponse? {
        val call = firebaseApi.create(FirebaseApi::class.java).getWeapon(id).execute()
        val weapon = call.body()
        weapon?.id = id
        return weapon
    }

    fun setWeapon(weapon: WeaponResponse): PostResponse? {
        val call = firebaseApi.create(FirebaseApi::class.java).setWeapon(weapon).execute()
        val results = call.body()
        return results
    }
}
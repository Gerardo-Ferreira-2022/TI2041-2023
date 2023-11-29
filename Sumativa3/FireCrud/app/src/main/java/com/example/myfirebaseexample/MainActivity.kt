package com.example.myfirebaseexample

import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.provider.Settings.Global
import android.view.Gravity
import android.widget.ArrayAdapter
import android.widget.Button
import android.widget.EditText
import android.widget.Spinner
import android.widget.Toast
import com.example.myfirebaseexample.api.FirebaseApiAdapter
import com.example.myfirebaseexample.api.response.WeaponResponse
import kotlinx.coroutines.Deferred
import kotlinx.coroutines.GlobalScope
import kotlinx.coroutines.async
import kotlinx.coroutines.Dispatchers
import kotlinx.coroutines.runBlocking

class MainActivity : AppCompatActivity() {
    // Referenciar campos de las interfaz
    private lateinit var idSpinner: Spinner
    private lateinit var nameField: EditText
    private lateinit var damageField: EditText
    private lateinit var costField: EditText
    private lateinit var buttonSave: Button
    private lateinit var buttonLoad: Button

    // Referenciar la API
    private var firebaseApi = FirebaseApiAdapter()

    // Mantener los nombres e IDs de las armas
    private var weaponList = arrayListOf<String>()

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        idSpinner = findViewById(R.id.idSpinner)
        nameField = findViewById(R.id.nameField)
        damageField = findViewById(R.id.damangeField)
        costField = findViewById(R.id.costField)

        buttonLoad = findViewById(R.id.buttonLoad)
        buttonLoad.setOnClickListener {
            Toast.makeText(this, "Cargando información", Toast.LENGTH_SHORT).show()
            runBlocking {
                getWeaponFromApi()
            }
        }

        buttonSave = findViewById(R.id.buttonSave)
        buttonSave.setOnClickListener {
            Toast.makeText(this, "Guardando información", Toast.LENGTH_SHORT).show()
            runBlocking {
                sendWeaponToApi()
            }
        }

        runBlocking {
            populateIdSpinner()
        }
    }

    private suspend fun populateIdSpinner() {
        val response = GlobalScope.async(Dispatchers.IO) {
            firebaseApi.getWeapons()
        }
        val weapons = response.await()
        weapons?.forEach { entry ->
            weaponList.add("${entry.key}: ${entry.value.name}")
        }
        val weaponAdapter = ArrayAdapter(this, android.R.layout.simple_spinner_dropdown_item, weaponList)
        with(idSpinner) {
            adapter = weaponAdapter
            setSelection(0, false)
            gravity = Gravity.CENTER
        }
    }

    private suspend fun getWeaponFromApi() {
        val selectedItem = idSpinner.selectedItem.toString()
        val weaponId = selectedItem.subSequence(0, selectedItem.indexOf(":")).toString()
        println("Loading ${weaponId}... ")
        val weaponResponse = GlobalScope.async(Dispatchers.IO) {
            firebaseApi.getWeapon(weaponId)
        }
        val weapon = weaponResponse.await()
        nameField.setText(weapon?.name)
        damageField.setText(weapon?.damage)
        costField.setText("${weapon?.cost}")
    }

    private suspend fun sendWeaponToApi() {
        val weaponName = nameField.text.toString()
        val damage = damageField.text.toString()
        val cost = costField.text.toString().toLong()
        val weapon = WeaponResponse("", weaponName, damage, cost)
        val weaponResponse = GlobalScope.async(Dispatchers.IO) {
            firebaseApi.setWeapon(weapon)
        }
        val response = weaponResponse.await()
        nameField.setText(weapon?.name)
        damageField.setText(weapon?.damage)
        costField.setText("${weapon?.cost}")
    }
}

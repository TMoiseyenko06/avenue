import { useState, useEffect } from "react";
import axios from "axios";
import React from 'react';
import { View, ScrollView, Text } from 'react-native';
import { Card, Button, Checkbox, Title } from 'react-native-paper';
import DropDown from 'react-native-paper-dropdown'

type Tag = {
  id: number;
  label: string;
};

export default function AccountCreation (){
    const [selected, setSelected] = useState<number[]>([]);
    const [tags, setTags] = useState<Tag[]>([]);
    const [load, setLoad] = useState<boolean>(false);
    const [formInfo, setFormInfo] = useState({
    firstName: "",
    lastName: "",
  });

    useEffect(()=>{

        const fetchTags = async () => {
            const setOption = (list : Array<{[key: string]: any}>) => {
            const formattedTags = list.map((item) => ({
                id:item.id,
                label:item.name
            }))
            setTags(formattedTags)
            setLoad(true)
        }

        const response = await axios.get("http://localhost:5000/tag/get_all_tags")
        setOption(response.data)
        }
        
        fetchTags()

    })

    const handleCheckboxChange = (id: number) => {
        setSelected((prev) => {
            if (prev.includes(id)) {
                return prev.filter((item) => item !== id)
            } else {
                return [...prev, id]
            }
        })
    }
    
    const getSelectedLabels = () => tags.filter(tag => selected.includes(tag.id)).map(tag => tag.label).join(', ')

    return (
    <ScrollView contentContainerStyle={{ padding: 16 }}>
      <View style={{ flex: 1, justifyContent: 'center', alignItems: 'center' }}>
        <View style={{ width: '100%', maxWidth: 600 }}>
          <Card>
            <Card.Title title="Please Complete Your Registration" />
            <Card.Content>
              <View style={{ marginBottom: 16 }}>
                <Text style={{ marginBottom: 8 }}>Select Interests</Text>
                <DropDown
                  label={'Select Interests'}
                  mode={'outlined'}
                  visible={dropdownVisible}
                  showDropDown={() => setDropdownVisible(true)}
                  onDismiss={() => setDropdownVisible(false)}
                  value={selected}
                  setValue={setSelected}
                  list={tags.map(({ id, label }) => ({ label, value: id }))}
                  multiSelect
                />
                {load && tags.map(({ id, label }) => (
                  <Checkbox.Item
                    key={id}
                    label={label}
                    status={selected.includes(id) ? 'checked' : 'unchecked'}
                    onPress={() => handleCheckboxChange(id)}
                  />
                ))}
              </View>
              <Button mode="contained" onPress={}>
                Register
              </Button>
            </Card.Content>
          </Card>
        </View>
      </View>
    </ScrollView>
  );

}
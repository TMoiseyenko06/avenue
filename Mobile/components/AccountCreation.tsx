import React, { useEffect, useState } from "react";
import axios from "axios";
import { View, ScrollView, Text } from "react-native";
import { Card, Button } from "react-native-paper";
import MultiSelect from "react-native-multiple-select";

type Tag = {
  id: number;
  label: string;
};

export default function AccountCreation() {
  const [tags, setTags] = useState<Tag[]>([]);
  const [selectedItems, setSelectedItems] = useState<number[]>([]);
  const [load, setLoad] = useState<boolean>(false);
  const [formInfo, setFormInfo] = useState({
    firstName: "",
    lastName: "",
  });

  useEffect(() => {
    const fetchTags = async () => {
      try {
        const response = await axios.get("http://localhost:5000/tag/get_all_tags");
        const formattedTags = response.data.map((item: any) => ({
          id: item.id,
          label: item.name,
        }));
        setTags(formattedTags);
        setLoad(true);
      } catch (error) {
        console.error("Failed to fetch tags:", error);
      }
    };

    fetchTags();
  }, []);

  const handleSubmit = () => {
    console.log("Selected Interests:", selectedItems);
    console.log("Form Info:", formInfo);
  };

  return (
    <ScrollView contentContainerStyle={{ padding: 16 }}>
      <View style={{ flex: 1, justifyContent: "center", alignItems: "center" }}>
        <View style={{ width: "100%", maxWidth: 600 }}>
          <Card>
            <Card.Title title="Please Complete Your Registration" />
            <Card.Content>
              <View style={{ marginBottom: 16 }}>
                <Text style={{ marginBottom: 8 }}>Select Interests</Text>
                <MultiSelect
                  items={tags.map(tag => ({ id: tag.id, name: tag.label }))}
                  uniqueKey="id"
                  onSelectedItemsChange={(selected: any) => setSelectedItems(selected)}
                  selectedItems={selectedItems}
                  selectText="Pick Interests"
                  searchInputPlaceholderText="Search Tags..."
                  tagRemoveIconColor="#CCC"
                  tagBorderColor="#CCC"
                  tagTextColor="#000"
                  selectedItemTextColor="#CCC"
                  selectedItemIconColor="#CCC"
                  itemTextColor="#000"
                  displayKey="name"
                  searchInputStyle={{ color: "#CCC" }}
                  submitButtonColor="#48d22b"
                  submitButtonText="Confirm"
                  styleDropdownMenuSubsection={{ padding: 10 }}
                />
              </View>
              <Button mode="contained" onPress={handleSubmit}>
                Register
              </Button>
            </Card.Content>
          </Card>
        </View>
      </View>
    </ScrollView>
  );
}

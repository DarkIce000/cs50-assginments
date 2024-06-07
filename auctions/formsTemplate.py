from django import forms

class formCreate(forms.Form):
    title = forms.CharField(widget=forms.TextInput(attrs={
                                "class":"form-control my-2 form-control",
                                "name":"title"
                                }))

    Description = forms.CharField(label="Description",
                                   widget=forms.Textarea(attrs={
                                       "class":"form-control my-2",
                                        "name":"description"
                                        }))

    url = forms.CharField(label="URL of Image (optional)",
                           widget=forms.TextInput(attrs={
                                "class":"form-control my-2 form-control",
                                "name":"url",
                                "type":"url"
                                 }))

    category = forms.CharField(label="Category",
                                widget=forms.TextInput(attrs={
                                    "class" : "form-control form-control my-2",
                                    "name":"category"
                                    })) 

    initialBid = forms.CharField(label="Initial",
                                  widget=forms.TextInput(attrs={
                                    "class" : "form-control form-control my-2",
                                    "name":"initialBid",
                                    "type":"number"
                                    })) 


class formComment(forms.Form):
    title = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control", "type":"text"}))
    msg = forms.CharField(widget=forms.Textarea(attrs={"class":"form-control"}))

class formWatchlist(forms.Form):
    addToWatchlist = forms.BooleanField()

# forms endhere 
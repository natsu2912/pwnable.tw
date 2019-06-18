unsigned int __cdecl PROCESS(unsigned int *a1, int a2)
{
  int v2; // ecx
  unsigned int *i; // edi
  unsigned int v4; // edx
  unsigned int v5; // esi
  unsigned int *v6; // eax
  unsigned int result; // eax
  unsigned int v8; // et1
  unsigned int v9; // [esp+1Ch] [ebp-20h]

  v9 = __readgsdword(0x14u);
  puts("Processing......");
  sleep(1u);
  if ( a2 != 1 )
  {
    v2 = a2 - 2;
    for ( i = &a1[a2 - 1]; ; --i )
    {
      if ( v2 != -1 )
      {
        v6 = a1;
        do
        {
          v4 = *v6;
          v5 = v6[1];
          if ( *v6 > v5 )
          {
            *v6 = v5;
            v6[1] = v4;
          }
          ++v6;
        }
        while ( i != v6 );
        if ( !v2 )
          break;
      }
      --v2;
    }
  }
  v8 = __readgsdword(0x14u);
  result = v8 ^ v9;
  if ( v8 != v9 )
    sub_BA0();
  return result;
}